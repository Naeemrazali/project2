# Writeup: 3D-Object Detections


## Varying visibility of vehicles in point cloud 
![Screenshot from 2021-11-27 05-13-07](https://user-images.githubusercontent.com/38019946/143521575-b407ed64-25da-44fb-a312-2a19257bd18b.png)
![Screenshot from 2021-11-27 05-13-43](https://user-images.githubusercontent.com/38019946/143521582-2e50f4dd-2a98-45f0-918d-027c0710814b.png)
![Screenshot from 2021-11-27 05-13-59](https://user-images.githubusercontent.com/38019946/143521587-9b269972-af09-46d3-b077-e7479df0bfd9.png)
![Screenshot from 2021-11-27 05-14-44](https://user-images.githubusercontent.com/38019946/143521591-e15b5574-bf84-4fcb-8261-ff0328a2eebc.png)
![Screenshot from 2021-11-27 05-15-17](https://user-images.githubusercontent.com/38019946/143521592-9b1bafd2-d02a-4f88-84f5-ba5d6e3618af.png)
![Screenshot from 2021-11-27 05-15-35](https://user-images.githubusercontent.com/38019946/143521594-88bba32d-e1f7-4d58-9ad9-a381cacc497f.png)
![Screenshot from 2021-11-27 05-16-07](https://user-images.githubusercontent.com/38019946/143521598-f4d2776d-c976-44bd-a7fe-a4f9015b20be.png)
![Screenshot from 2021-11-27 05-16-47](https://user-images.githubusercontent.com/38019946/143521601-319cfcef-5542-43d7-91b0-1fa818f7ebd7.png)
![Screenshot from 2021-11-27 05-17-06](https://user-images.githubusercontent.com/38019946/143521604-2556a47e-bcfd-4779-b2fa-df80552b21ba.png)
![Screenshot from 2021-11-27 05-17-28](https://user-images.githubusercontent.com/38019946/143521609-ebd70743-32c2-460c-b8cd-28b4eccb74e9.png)
![Screenshot from 2021-11-27 05-17-44](https://user-images.githubusercontent.com/38019946/143521613-ac6974c8-dd15-40de-9584-21bb0f7d0cf0.png)


## Vehicle features

![Screenshot from 2021-11-27 05-21-03](https://user-images.githubusercontent.com/38019946/143521835-5cdf5b59-c3b1-41ff-836b-c452413f665f.png)
![Screenshot from 2021-11-27 05-21-53](https://user-images.githubusercontent.com/38019946/143521906-e700a278-920f-4e57-a39a-0cbd2b0ba76d.png)

The two images above show examples of the front bumper of vehicles. They can be identified from the point cloud by the shape and density of points. As most car bumpers are around the same height intensity of objects at this height can be used to identify most cars. 

The rear bumper of vehicles can be also be identified in a similar manner, as can be seen by the point cloud images below:

![Screenshot from 2021-11-26 21-30-17](https://user-images.githubusercontent.com/38019946/143551040-34a05ce9-0c32-4460-abc3-908c82b3f03b.png)
![Screenshot from 2021-11-26 21-33-27](https://user-images.githubusercontent.com/38019946/143551054-29e76538-dc99-4541-9691-ec4d24a796cb.png)

By taking the intensity map of these point clouds it can be seen that the front and rear bumpers can be easily discerned. This can be seen in the below screenshots of parts of an intensity map:

![Screenshot from 2021-11-26 21-45-21](https://user-images.githubusercontent.com/38019946/143553031-811067cf-2611-4811-937f-cfc07e9dc85a.png)
![Screenshot from 2021-11-26 21-45-51](https://user-images.githubusercontent.com/38019946/143553033-dce98574-e528-450d-93a4-5861bc505e75.png)









