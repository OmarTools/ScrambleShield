# ScrambleShield
- ScrambleShield is a free and open-source Image obscurity tool for securely sending images. It works by splitting the image into multiple parts, applying random transformations (currently rotations only) and then saving the transformation details in a separate text file. The recipient uses this "key" file to reverse the process and reconstruct the original image.
- ScrambleShield doesn't offer encryption, it can be a valuable tool for situations where you want to add an extra layer of protection to shared images, especially if combined with strong key management practices.
## How to use:
 - open split.py with Notepad then write the image path and output folder location 
 - specify number of parts for example if you write 40 it means 40x40
  ![Screenshot 2024-06-25 142601](https://github.com/OmarTools/ScrambleShield/assets/165505995/d0607812-8ec3-4e83-bbde-c49c84cefa50)
 - write in address bar where the script is located "cmd" then type the name of the python file in the cmd which is split.py in this case
 - and that is it the image is split!!
 - do the same with unsplit.py file to restore the image
### Extra Versions Note:
- mpsplit.py implemented to work using multiprocessing ,**split.py is recommended for shorter splits**
- unsplitmp.py introduce a dictionary to store the opened part images especially when dealing with a large number of part images,**unsplit.py is recommended for shorter splits** 
 

## Suggested enhancements/future work:
- adding more transformations like mirroring
- adding random brightness and contrast adjustments **(not recommended as the reversed parts will not look the exact same as the original image)**
- adding more complex transformations like cropping or pixel shuffling for enhanced security.
- adding more image scrambling techniques. visit: https://www.researchgate.net/publication/331064749_Cryptographic_image_Scrambling_techniques
