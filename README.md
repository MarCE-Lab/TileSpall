# TileSpall
This dataset comprises **364 images of tile spalling on building façades**, collected to support research on façade damage detection and segmentation. The dataset is designed to reflect real-world variability in spalling appearance and building conditions.

## Overview

- **Images:** 364 real-world RGB images  
- **Annotations:** Pixel-wise binary masks (in PNG format)  
- **Domain:** Urban buildings with tile detachment (spalling)  
- **Geographic scope:** Multiple cities in Taiwan  

## Data Collection

To ensure diversity in spalling appearance and environmental conditions:

- **90%** of images were sourced from **Google Street View**
- **6.5%** from smartphone photography
- **3.5%** from **social media platforms**

## Example Images

<table>
  <tr>
    <td align="center"><b>Original</b></td>
    <td align="center"><b>Mask</b></td>
  </tr>
  <tr>
    <td><img src="figures/image1.png" width="200"/></td>
    <td><img src="figures/mask1.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="figures/image2.png" width="200"/></td>
    <td><img src="figures/mask2.png" width="200"/></td>
  </tr>
  <tr>
    <td><img src="figures/image3.png" width="200"/></td>
    <td><img src="figures/mask3.png" width="200"/></td>
  </tr>
</table>

> *Each column shows an original image (left) and its manually annotated mask (right). Spalling areas are marked in white.*

## Download

You can download the dataset from the following link:

🔗 **[https://ce13078.ce.ntu.edu.tw/open_datasets/spalling_data.zip](https://ce13078.ce.ntu.edu.tw/open_datasets/spalling_data.zip)**

Or use the command-line to download and unzip:

```bash
wget https://ce13078.ce.ntu.edu.tw/open_datasets/spalling_data.zip
unzip spalling_data.zip
```
## License

Details included in the LICENSE file.
