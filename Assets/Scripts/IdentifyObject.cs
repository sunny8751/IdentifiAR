using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using UnityEngine.UI;
using System;

public class IdentifyObject : MonoBehaviour {

    //public byte[] imageData;

    // Use this for initialization
    public void Identify (string filePath) {
        //Make a new form
        WWWForm form = new WWWForm();

		//Create and attach headers
		var headers = form.headers;
		headers["Ocp-Apim-Subscription-Key"] = "5c650f97fd8a4410a168c813c61bbe4c";
		headers ["Content-Type"] = "application/octet-stream";

		//Declare byte array of image to be sent
		byte[] imageData = null;

        //You can either add straight into function or pull from storage
        //fileName = Path.Combine(Application.streamingAssetsPath, fileName);
        FileInfo fileInfo = new FileInfo(filePath);
		long imageFileLength = fileInfo.Length;
		FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
		BinaryReader br = new BinaryReader(fs);

		//Map image into byte array
		imageData = br.ReadBytes((int)imageFileLength);

		string url = "https://eastus2.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Description";
		//https://[location].api.cognitive.microsoft.com/vision/v1.0/analyze[?visualFeatures][&details][&language]

		WWW www = new WWW(url, imageData, headers);
		StartCoroutine(WaitForRequest(www));
	}

	IEnumerator WaitForRequest(WWW www)
	{
		yield return www;
		// check for errors
		if (www.error == null)
		{
			//Do something with response
			Debug.Log("WWW Ok!: " + www.text);
            ItemInfo.SetSuccess(www.text);
        } else {
			Debug.Log("WWW Error: "+ www.error);
            ItemInfo.SetFail(www.text);
        }
	}
}
