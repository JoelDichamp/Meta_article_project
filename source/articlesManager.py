import pathlib 
import shutil
from typing import Tuple, List, Dict
import json
import utils


def articleExists(articleName: str) -> bool:
  p = utils.dataFolder / articleName
  return p.exists()


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
      if ext == utils.EXT_TAGS:
        p_dest = utils.dataFolder / articleName / utils.FILE_TAGS
      else:
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


def checkTagsFile(jsonFile: pathlib.Path) -> Tuple[bool, str, List[str]]:
  listTags = []
  ok = False
  error_msg = f'File {jsonFile}: list[str] expected!\nThe list of tags will be empty.'

  with open(jsonFile, "r") as f:
    try:
      obj = json.load(f)
      if type(obj).__name__ == 'list':
        if len(obj) > 0:
          if type(obj[0]).__name__ == 'str':
            listTags = obj
            ok = True
        else:
          ok = True

    except json.decoder.JSONDecodeError as e:
      # json vide ou autre pb de decoder, on retourne une liste vide
      error_msg = f'File {jsonFile}: {e}\nThe list of tags will be empty.'

  return ok, error_msg, listTags


def getTagsArticle(article : pathlib.Path, d: Dict) -> Dict:
  p = article / utils.FILE_TAGS
  if p.exists():
    ok, msg , listTags = checkTagsFile(p)
    strTags = ' '.join(listTags)
    if ok:
      d[utils.D_TAGS] = strTags
      d[utils.D_PATH_TAGS] = p
    else:
      d[utils.D_TAGS] = msg
      d[utils.D_PATH_TAGS] = pathlib.Path()
  else:
    d[utils.D_TAGS] = f"File '{utils.FILE_TAGS}' not found!"
    d[utils.D_PATH_TAGS] = pathlib.Path()

  return d

  
def fillDict(s_d_ext: str, s_d_path_ext: pathlib.Path, d: Dict, ext: str) -> Dict:
  if ext == utils.EXT_PDF:
    d[utils.D_PDF] = s_d_ext
    d[utils.D_PATH_PDF] = s_d_path_ext
  elif ext == utils.EXT_NOTES:
    d[utils.D_NOTES] = s_d_ext
    d[utils.D_PATH_NOTES] = s_d_path_ext
  elif ext == utils.EXT_TAGS:
    d[utils.D_TAGS] = s_d_ext
    d[utils.D_PATH_TAGS] = s_d_path_ext

  return d


def getFilesArticle(article : pathlib.Path, d: Dict, ext: str) -> Dict:
  p = article / (article.name + ext)
  if p.exists():
    d = fillDict(article.name + ext, p, d, ext)
  else:
    d = fillDict(f"File '{ext}' not found!", pathlib.Path(), d, ext)

  return d


def checkFileName(articleName: str, f : pathlib.Path, ext: str) -> Tuple[bool, str]:
  ok = True
  error_msg = ''

  if (f.name != (articleName + ext)) or (ext == utils.EXT_TAGS and f.name != utils.FILE_TAGS):
    ok, error_msg = copyToDataFolder(articleName, str(f), ext, 'move')

  return ok, error_msg


def getArticles(search: bool = False, articles: List[pathlib.Path] = []) -> Dict:
  dictArticles = {}
  if not search:
    articles = [f for f in utils.dataFolder.iterdir() if f.is_dir()]
  for article in articles:
    keyArticle = article.stem
    dictArticles[keyArticle] = {}
    dictArticles[keyArticle][utils.D_PATH_ARTICLE] = article

    word_ok = False
    pdf_ok = False
    json_ok = False
    for f in article.iterdir():
      ext = f.suffix.lower()
      if ((not word_ok) and (ext == utils.EXT_NOTES)) or ((not pdf_ok) and (ext == utils.EXT_PDF)) or ((not json_ok) and (ext == utils.EXT_TAGS)):
        ok, error_msg = checkFileName(keyArticle, f, ext)
        if ok:
          if ext == utils.EXT_NOTES or ext == utils.EXT_PDF:
            dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], ext)
            if ext == utils.EXT_NOTES: 
              word_ok = True 
            else: 
              pdf_ok = True
          else: # ext == utils.EXT_TAGS
            dictArticles[keyArticle] = getTagsArticle(article, dictArticles[keyArticle])
        else:
          dictArticles[keyArticle] = fillDict(error_msg, pathlib.Path(), dictArticles[keyArticle], ext)

    if not word_ok:
      dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_NOTES)
    if not pdf_ok:
      dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_PDF) 
    if not json_ok:
      dictArticles[keyArticle] = getTagsArticle(article, dictArticles[keyArticle])

  return dictArticles


# def getTagsArticle(article : pathlib.Path, d: Dict) -> Dict:
#   p = article / utils.FILE_TAGS
#   if p.exists():
#     listTags = checkTagsFile(p)
#     strTags = ' '.join(listTags)
#     d[utils.D_TAGS] = strTags
#     d[utils.D_PATH_TAGS] = p
#   else:
#     d[utils.D_TAGS] = f"File '{utils.FILE_TAGS}' not found!"
#     d[utils.D_PATH_TAGS] = ''

#   return d


# def getFilesArticle(article : pathlib.Path, d: Dict, ext: str, d_file: str, d_pathFile: str) -> Dict:
#   p = article / (article.name + ext)
#   if p.exists():
#     d[d_file] = article.name + ext
#     d[d_pathFile] = p
#   else:
#     d[d_file] = f"File '{d_file}' not found!"
#     d[d_pathFile] = ''

#   return d
  

# def getArticles(search: bool = False, articles: List[pathlib.Path] = []) -> Dict:
#   dictArticles = {}

#   if not search:
#     articles = [f for f in utils.dataFolder.iterdir() if f.is_dir()]
#   for article in articles:
#     keyArticle = article.stem
#     dictArticles[keyArticle] = {}
#     dictArticles[keyArticle][utils.D_PATH_ARTICLE] = article

#     dictArticles[keyArticle] = getTagsArticle(article, dictArticles[keyArticle])
#     dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_PDF, utils.D_PDF, utils.D_PATH_PDF)
#     dictArticles[keyArticle] = getFilesArticle(article, dictArticles[keyArticle], utils.EXT_NOTES, utils.D_NOTES, utils.D_PATH_NOTES)

#   return dictArticles


def _printDictArticles(d):
  for x in d:
    print(x)
    for y in d[x]:
      print(y, ':', d[x][y])

    print("-" * 50)

if __name__ == "__main__":
  d = getArticles()
  _printDictArticles(d)