using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using SimpleJSON;

public class ItemInfo : MonoBehaviour {

    public static void SetSuccess(string s)
    {
        var N = JSON.Parse(s);
        string val = N["description"]["captions"][0]["text"];
        SetDescription(val);
    }

    public static void SetFail(string s)
    {
        SetDescription("Error");
    }

    public static void Clear(string s)
    {
        GameObject.FindWithTag("Description").GetComponent<Text>().text = "Description: " + s;
    }

    private static void SetDescription(string s)
    {
        GameObject.FindWithTag("Description").GetComponent<Text>().text = "Description: " + s;
    }
}
