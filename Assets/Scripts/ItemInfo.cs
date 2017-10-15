using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using SimpleJSON;

public class ItemInfo : MonoBehaviour {

	// Use this for initialization
	void Start () {
    }

    public static void SetSuccess(string s)
    {

    }

    public static void SetFail(string s)
    {
        GameObject.FindWithTag("Description").GetComponent<Text>().text = "Description: " + s;
    }

    public static void Clear(string s)
    {
        GameObject.FindWithTag("Description").GetComponent<Text>().text = "Description: " + s;
    }

    private static SetDescription(string s)
    {
        GameObject.FindWithTag("Description").GetComponent<Text>().text = "Description: " + s;
    }
}
