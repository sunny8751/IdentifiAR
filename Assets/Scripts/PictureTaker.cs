using UnityEngine;
using System;
using System.Linq;
using UnityEngine.XR.WSA.WebCam;

using System.IO;

/*
Purpose of Scanning class: 
    - Capture a snapshot from the webcam
    - call APIHandler.cs to make request for object recognition using snapshot
    - call Coordinate.cs to create bounding box of the recognizable objects
*/
public class PictureTaker : MonoBehaviour
{
    /*----------------------------------ALL DECLARATIONS---------------------------------------------*/

    public int pixelWidth;
    public int pixelHeight;

    /* represents the coordinates of the camera (x,y,z) */
    public Vector3 lastCameraPosition;

    /* representS the rotation of the camera (x,y,z,w) */
    public Quaternion lastCameraAngle;

    /* object to capture a photo of surroundings */
    PhotoCapture photoCaptureObject = null;

    /* private strings used for the photo taken */
    public string filename = "";
    public string filepath = "";

    /* -------------------------------------------------------------ALL METHODS----------------------------------------------------------- */

    public void Start()
    {
        /* initialize pixelWidth, pixelHeight, voice (txtToSpeech), and classes */

        pixelWidth = Camera.main.pixelWidth;

        pixelHeight = Camera.main.pixelHeight;
        //TakePicture();
    }

    /* 
    Asynchronously creates an instance of a PhotoCapture 
    object that can be used to capture photos. 
    Function called by VoiceController.cs
    */
    public void TakePicture()
    {
        lastCameraPosition = Camera.main.transform.position;
        //lastCameraPosition = Camera.main.gameObject.transform.position;

        lastCameraAngle = Camera.main.transform.rotation;
        //lastCameraAngle = Camera.main.gameObject.transform.rotation;

        PhotoCapture.CreateAsync(false, OnPhotoCaptureCreated);
    }

    /*
	Initializes settings that the web camera will use
    Function called by TakePhoto
	*/
    void OnPhotoCaptureCreated(PhotoCapture captureObject)
    {
        Debug.Log("Photocapture");

        photoCaptureObject = captureObject;

        /* setting up camera resolution */
        Resolution cameraResolution = PhotoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();

        CameraParameters c = new CameraParameters();

        /* setting the opacity of captured holograms */
        c.hologramOpacity = 0.0f;

        /* valid resolutions for use with the web camera */
        c.cameraResolutionWidth = cameraResolution.width;
        c.cameraResolutionHeight = cameraResolution.height;

        /* pixel format to capture & record image data */
        c.pixelFormat = CapturePixelFormat.BGRA32;

        /* Activate mode to take photo */
        captureObject.StartPhotoModeAsync(c, OnPhotoModeStarted);
    }

    /*
	Save the captured image passed as a paramter (result)
    Function called by OnPhotoCaptureCreated
	*/
    private void OnPhotoModeStarted(PhotoCapture.PhotoCaptureResult result)
    {
        /* camera was not successfully activated */
        if (!result.success)
        {
            Debug.LogError("Unable to start photo mode!");
            return;
        }

        /* camera was successfully activated */
        Debug.Log("Photo Mode Started");

        /* save name and path in computer */
        filename = string.Format(@"CapturedImage{0}_n.jpg", Time.time);
        filepath = Path.Combine(Application.persistentDataPath, filename);

        /* try and capture photo from the camera */
        try
        {
            photoCaptureObject.TakePhotoAsync(filepath, PhotoCaptureFileOutputFormat.JPG, OnCapturedPhotoToDisk);

            Debug.Log("Picure was successfully taken");
        }
        catch (ArgumentException e)
        {
            Debug.LogError("System.ArgumentException:\n" + e.Message);
        }

        Debug.Log("Saving photo to Filepath: " + filepath);
        Debug.Log("Saving photo as Filename: " + filename);
    }

    /*
    Send API request through APIHandler.cs and create bounding box with Coordinate.cs
    Function called by OnPhotoModeStarted
    */
    public void OnCapturedPhotoToDisk(PhotoCapture.PhotoCaptureResult result)
    {
        /* if photo was not successfully saved to disk */
        if (!result.success && !File.Exists(filepath))
        {
            Debug.Log("Failed to save Photo to disk");
            return;
        }


        Debug.Log("Saved Photo to disk!");

        /* function call to stop camera photo mode */
        photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);

        /* call function to make api call */
        GameObject.Find("ImageRecognition").GetComponent<IdentifyObject>().Identify(filepath);
    }

    /*
    Deactivates photo mode
    Function called by OnCapturedPhotoToDisk
	*/
    void OnStoppedPhotoMode(PhotoCapture.PhotoCaptureResult result)
    {
        photoCaptureObject.Dispose();
        photoCaptureObject = null;
    }
}