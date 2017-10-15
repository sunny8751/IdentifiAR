using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.WSA.Input;


public class GazeGestureManager : MonoBehaviour
{
    public static GazeGestureManager Instance { get; private set; }

    UnityEngine.XR.WSA.Input.GestureRecognizer recognizer;

    // Use this for initialization
    void Start()
    {
        Instance = this;

        // Set up a GestureRecognizer to detect Select gestures.
        recognizer = new GestureRecognizer();
        recognizer.TappedEvent += OnTappedEvent;
        //recognizer.HoldStartedEvent += OnHoldStartedEvent;
        recognizer.StartCapturingGestures();
    }

    //public void OnHoldStartedEvent(InteractionSourceKind source, Ray headRay)
    //{
    //    GameObject.FindWithTag("Information").GetComponent<Text>().text = "Hold Gesture has been made!";
    //}

    public void OnTappedEvent(InteractionSourceKind source, int tapCount, Ray headRay)
    {
        recognizer.CancelGestures();
        GameObject.Find("ImageRecognition").GetComponent<PictureTaker>().TakePicture();
        recognizer.StartCapturingGestures();
    }
}