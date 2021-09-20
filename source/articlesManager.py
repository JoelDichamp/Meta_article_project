import pathlib 
import shutil
from typing import Tuple
import json
import utils


def articleExists(articleName: str) -> bool:
  p = utils.dataFolder / articleName
  return p.exists()

  # dirs = [f for f in utils.dataFolder.iterdir() if f.is_dir() and f.stem == articleName]
  # exists = len(dirs) == 1
  # print(dirs, exists)
  # return exists


def articleAlreadyUsed(fct: str, articleName: str, articleOri: str = '') -> bool:
  alreadyUsed = False

  if articleExists(articleName):
    if fct == utils.FCT_CREATE:
      alreadyUsed = True
    elif fct == utils.FCT_UPDATE:
      if articleName.lower() != articleOri.lower():
        alreadyUsed = True

  return alreadyUsed


def copyToDataFolder(articleName: str, fullFile: str, ext: str, action: str = 'copy') -> Tuple[bool, str]:
  error_msg = ''
  ok = True

  if fullFile:
    p_fullFile = pathlib.Path(fullFile)
    if p_fullFile.name != (articleName + p_fullFile.suffix):
      p_dest = utils.dataFolder / articleName / (articleName + ext)
      try:
        if action == 'copy':
          shutil.copy(p_fullFile, p_dest)
          # print(f"Copy ok : {p_fullFile} -> {p_dest}")
        elif action == 'move':
          shutil.move(p_fullFile, p_dest)
      except:
        ok = False
        error_msg = f"Error '{action} : {p_fullFile}' to '{p_dest}'"

  return ok, error_msg


def copyTags(articleName: str, tags: str) -> None:
  listTags = tags.split()
  p_dest = utils.dataFolder / articleName / utils.FILE_TAGS
  with open(p_dest, "w") as f:
    json.dump(listTags, f, indent=4)

def renameFilesPdfNotes(articleName: str, fileName: str) -> str:
  p = pathlib.Path(fileName)
  newFile = utils.dataFolder / articleName / p.name

  return str(newFile)


def majArticle(fct: str, articleName: str, articleOri: str = '', tags: str = '', pdf: str = '', notes: str = '') -> Tuple[bool, str]:
  error_msg = ''
  ok = True

  if articleAlreadyUsed(fct, articleName, articleOri):
    return False, f"The meta-article '{articleName}' already exists!"

  action = 'copy'
  if fct == utils.FCT_CREATE:
    p = utils.dataFolder / articleName
    p.mkdir()
  elif fct == utils.FCT_UPDATE:
    if articleName != articleOri:
      p = utils.dataFolder / articleOri
      p.rename(utils.dataFolder / articleName)
      pdf = renameFilesPdfNotes(articleName, pdf)
      notes = renameFilesPdfNotes(articleName, notes)
      action = 'move'

  ok, error_msg = copyToDataFolder(articleName, pdf, utils.EXT_PDF, action)
  if ok:
    ok, error_msg = copyToDataFolder(articleName, notes, utils.EXT_NOTES, action)
  if ok:
    copyTags(articleName, tags)

  return ok, error_msg
  

def removeArticle(articleName: str) -> Tuple[bool, str]:
  error_msg = ''
  ok = False

  if articleExists(articleName):
    try:
      shutil.rmtree(utils.dataFolder / articleName) 
      ok = True
    except:
      error_msg = f"Error when deleting '{articleName}'"
  else:
    error_msg = f"The meta-article '{articleName}' cannot be found!"

  return ok, error_msg


def getTagsArticle(article : pathlib.Path, d: dict):
  p = article / utils.FILE_TAGS
  if p.exists():
    with open(p, "r") as f:
      listTags = json.load(f)
      strTags = ' '.join(listTags)
      d[utils.D_TAGS] = strTags
      d[utils.D_PATH_TAGS] = p
  else:
    d[utils.D_TAGS] = f"File '{utils.FILE_TAGS}' not found!"
    d[utils.D_PATH_TAGS] = ''

  return d


def getFilesArticle(article : pathlib.Path, d: dict, ext: str, d_file: str, d_pathFile: str):
  p = article / (article.name + ext)
  if p.exists():
    d[d_file] = article.name + ext
    d[d_pathFile] = p
  else:
    d[d_file] = f"File '{d_file}' not found!"
    d[d_pathFile] = ''

  return d


def getArticles(search: bool = False, articles: list[pathlib.Path] = []):
  dictArticles = {}

  if not search:
    articles = [f for f in utils.dataFolder.iterdir() if f.is_dir()]
  for article in articles:
    keyArticle = article.stem
    dictArticles[keyArticle] = {}
    dictArticles[keyArticle][utils.D_PATH_ARTICLE] = article

    dictArticles[keyArticle] = getTagsArticle(article, dictArticles[keyArticle])
    dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_PDF, utils.D_PDF, utils.D_PATH_PDF)
    dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_NOTES, utils.D_NOTES, utils.D_PATH_NOTES)

  return dictArticles


def _printDictArticles(d):
  for x in d:
    print(x)
    for y in d[x]:
      print(y, ':', d[x][y])

    print("-" * 50)

if __name__ == "__main__":
  d = getArticles()
  _printDictArticles(d)