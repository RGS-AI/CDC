# CDC
## Cast Defect Model using CNN for Submersible Pump Impeller

Introduction:
Casting is a manufacturing process where molten metal is poured into a mold and allowed to solidify, forming a desired shape. It is widely used in industries like automotive, aerospace, and machinery due to its ability to produce complex shapes cost-effectively.

Common Casting Defects
Defects in casting occur due to improper process parameters, materials, or environmental conditions. Some common defects include:

Porosity: Small air pockets or voids formed inside the casting.
Shrinkage: Cavities caused by volume reduction during metal solidification.
Cracks: Surface or internal cracks due to thermal stresses.
Misruns: Incomplete filling of the mold, leading to incomplete parts.
Surface Defects: Irregularities like roughness, inclusions, or cold shuts on the surface.
Significance of Defect Detection
Detecting casting defects early is critical because:

Defects compromise product quality and functionality.
  1. Manual inspection is time-consuming and prone to errors.
  2. Automated solutions using Computer Vision and Deep Learning enable faster, more accurate defect detection, reducing production costs and ensuring quality.

The dataset is imported from Kaggle, and is trained with CNN model having 2 Conv2D layers, a flattening layer and dense or fully connected layers. With the accuracy of 94.82%, the model is saved as .h5 and is tested for further evaluation. The prediction is good with the current parameters, however, it could be improved over by adding dropout layers, early stopping and learning transfer.

A Huge shout out to the dataset provider ravirajsinhdabhi86@gmail.com - https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product/data
Thanks to https://www.kaggle.com/code/sayooj98/gear-fault-diagnosis-using-cnn/notebook for the idea behind it and coding part. 

My future edit shall include but not limited to early stopping, learning rate and transfer learning.

The same is deployed for application. 
https://www.testcdc.streamlit.io

Thank you,

RMS