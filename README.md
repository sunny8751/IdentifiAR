# IdentifiAR
Shop smartly. With IdentifiAR, make calculated purchases instantly with product research at your fingertips.

![Logo](https://raw.githubusercontent.com/sunny8751/IdentifiAR/master/Assets/Images/logo.jpg)

![Demo](https://raw.githubusercontent.com/sunny8751/IdentifiAR/master/Assets/Images/demo.jpg)

## What inspired us
Inspired by Amazon’s push towards Amazon Go and the “grocery store of the future,” we took our passion for augmented reality and built the experience we've always dreamed of living.

Revolutionizes the “point of sale” aspect of shopping by giving the consumer all the relevant information they need to make an informed purchase, including alternative choices to drive pro-consumer competition. As over 60% of buying decisions are made at the point of sale, it is critical that we provide as much insight to the customer as possible during this time period.

## What it does
Wear the HoloLens and make a pinching gesture to take a picture of the product you are looking at. A computer vision algorithm analyzes this photo and returns information about the item.

## How we built it
We knew we wanted to work with the HoloLens for its strong AR capabilities, with the Microsoft Azure cognitive computer API for its computer vision properties, and with the NCR API for the extensive transactional dataset.

We used the Unity platform to integrate with the HoloLens. The picture that was taken was sent to Azure's Computer Vision API, which generated a list of discriptive tags about the object. We compared those tags to a Python script that utilized the NCR API to provide specific product information.

## Challenges we ran into
* The NCR API was tricky to work with, as many API calls had required params that could only be gotten through another API calls, and thus we were stuck for a little while, chaining calls together before we figured out a workaround. However, the NCR team was very helpful and provided invaluable insight into how their API calls should be constructed.

* In addition, we ran into a hardware issue an hour before submission that proved to be very difficult to work through, as we were all running on no sleep, which hampered our problem solving abilities. Thankfully, we were able to rally together and crack the bug.

## What we learned
As a team, we’re very happy with our end results - we took the HoloLens and Azure cognitive services API, technologies that none of us had worked with before, and successfully integrated these working components while navigating new APIs and overcoming the logistical hurdles of getting it done during a 36 hour hackathon.

In addition, we created a project that walks amongst the future of retail, and that’s something we’re very excited about.

## Related Links

* [Devpost](https://devpost.com/software/identifiar-j8kxcg) - The hackathon Devpost
* [Presentation](https://docs.google.com/presentation/d/1TVuZVnOWKhTIpvK3u4K8lHlXA7v_t8rY62DV8HyQ58Q/edit?usp=sharing) - Presentation

