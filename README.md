This is the ASCII Artwork Converter project!
There are multiple varibles that you can edit to change the ASCII:
"SINGLE_CHAR_HEIGHT", "SIGNLE_CHAR_WIDTH", "SCALE_FACTOR", "font", "chars".

IMPORTANT:
- For this to work, you need to have a .jpg file and specify its name in the "im" variable. Currently, that is line 20.
- If you are on a Windows / Macintosh machine, change the "font" varible path. This code was developed on Linux, and therefore the pathway will only work on Linux.

What each variable does:
- "SIGNLE CHAR_HEIGHT" : How tall each character within the ASCII will be.
- "SINGLE_CHAR_WIDTH" : How wide each character within the ASCII will be.
- "SCALE_FACTOR" : How scaled relative the the original resolution will be. To keep it more ASCII, I recommend 0.2 - 0.8 values.
- "font" : What font will be used, with its pathway specified.
- "chars" : All types of characters that can be used within the ASCII, they are listed from densest characters to the least densest. Ignore the [: : (-1)].

Optional:
- If you would also like to have a .txt file of the ASCII, simply uncomment lines with arrows pointing to them. As of right now, these are lines: 34, 64 and 66. 
