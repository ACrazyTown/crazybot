# crazyBot Changelog
## Version RELEASE-1.0
Version **RELEASE-1.0** is the first major release of crazyBot which is not a development build.

### Changes 
#### Overseer
* Added logging system
  * Replaces the old `print()` system using the `logging` module included in Python. Because of this, the Overseer can also print logs to file.
* Improved Updating system
  * Now includes a seperate `check_git()` function.
    * Checking is improved, instead of trying to run the `git` command, it uses `shutil.which` to find if Git is present.
  * Various improvements.
#### crazyCommands
* Cleaned & improved code
  * Using classes, the code is much cleaner and easier to read.
    * In categories, if only the prefix and category is specified (eg. `crazy debug`) the bot will use the Usage() command to tell the user the correct usage.
