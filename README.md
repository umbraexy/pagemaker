# pagemaker
A Python script that prints out a new "page" line in a .txt file every time you run it.

It first attempts to create a new file called "scroll_z.txt". If it is succesful at it, it will add "page0" to its content.
However, if the file already exists (either because you are running the script a second time or the .txt file was already there), it will simply append a subsequent page to it. (a.k.a page1).
The script is formulated so that every time the script is ran the next appended page will always be one number up the previous page, up to 9. It doesn't matter whether you modify your page to 0,3,8, the script will always run append the next sequential page.
Once it reaches 10, the script will delete "scroll_z.txt", allowing you to re-run the program from start.

I created this script to apply try/except and open() mostly.
