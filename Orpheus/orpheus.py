import requests
import base64
import json
import sys
from secrets import * 

# === Script Arguments ===
args = sys.argv
songName=args[1]
artistName=args[2]
print(songName+" "+artistName)




# ===  Authorization ===

clientId='e4035c3d93cf45bf8b9084a5915fc520'
clientSecret='d137134f3c354b4487f1fa38c43247b8'

# === Encoding ===

message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')

# === Token ===

url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']
headers = {
    "Authorization": "Bearer " + token 
}

# === Spotify Search ===

def spotifySearch(songName,artistName):
    searchUrl=f'https://api.spotify.com/v1/search?q=track%3A{songName}+artist:{artistName}&type=track%2Cartist&limit=1'
    res = requests.get(url=searchUrl, headers=headers)
    
    responseObject = json.dumps(res.json())
    tracksArray = json.loads(responseObject)["tracks"]["items"]
    for track in tracksArray:
        output=track["id"]
    return output
    # print(output)
    
# =-== Mood Finder ===

def spotifySongCharacteristics(songId):
    searchUrl=f"https://api.spotify.com/v1/audio-features/{songId}"
    res = requests.get(url=searchUrl, headers=headers)
    # print(json.dumps(res.json()))
    # txt.write(json.dumps(res.json(), indent=2))
    moodFinder(json.dumps(res.json()))

def moodFinder(res):
    characteristicDict=json.loads(str(res))
    danceability=characteristicDict["danceability"]
    energy=characteristicDict["energy"]
    valence=characteristicDict["valence"]
    tempo=characteristicDict["tempo"]
    key=characteristicDict["key"]
    # energy X axis : energy, tempo
    # feel Y axis: valence, danceablitlity, key

    energyValue=abs(round((energy+((tempo-110)/50))*1.7/3,4))
    
    feelValue=abs(round((2*valence+danceability+musicalKeyValue(key))/4,4))
    # print("  - energy: "+str(energyValue))
    # print("  - feel: "+str(feelValue))
    # print("d:"+str(danceability)+" e:"+str(energy)+" v:"+str(valence)+" t:"+str(tempo)+" k:"+str(key))
    moodListColor=['e8e8e8','d9526d','d9c5f0','adbbed','e3c18a','ebe68a','d1f0de','daeba4']
    moodListName=['flow','angry','guilt','sad','anxious','happy','hope','loving']
    moodListAxisX=[0.5,0.2,0.35,0.3,0.4,0.65,0.65,0.9] #energy axis
    moodListAxisY=[0.5,0.9, 0.5,0.3,0.8,0.85,0.5,0.65] #feel axis
    
    smallestDiff=2
    indexOfSmallestDiff=0
    for i in range(len(moodListName)):
        diff=abs(energyValue-moodListAxisX[i])+abs(feelValue-moodListAxisY[i])
        if(smallestDiff>diff):
            smallestDiff=diff
            indexOfSmallestDiff=i
        # print(str(moodListName[i])+" "+str(diff))
    print("  - mood: "+moodListName[indexOfSmallestDiff])    
    print("  - color: "+moodListColor[indexOfSmallestDiff])
    
    txt = open("mood.txt", "w")
    txt.write(moodListName[indexOfSmallestDiff]+'\n'+moodListColor[indexOfSmallestDiff])   
    
    
def musicalKeyValue(key):
    value=0
    if key == -1: #No key
        value=0 
    if key == 0: # C
        value=0.7
    if key == 1: # C#
        value=0.25
    if key == 2: # D
        value=0.6
    if key == 3: # D#
        value=0.35
    if key == 4: # E
        value=0.45
    if key == 5: # F
        value=0.30
    if key == 6: # F#
        value=0.60
    if key == 7: # G
        value=0.55
    if key == 8: # G#
        value=0.25
    if key == 9: # A
        value=0.7
    if key == 10: # A#
        value=0.45
    if key == 11: # B
        value=0.4
    return value
    
# === Result ===

tempId=spotifySearch(songName,artistName)
spotifySongCharacteristics(tempId)
    
    
# === Testing Code ===

# txt.write(json.dumps(res.json(), indent=2))

# songList=['uprising','pretty when you cry','around the world','tobacco sunburst','head over heels','mountain at my gates',
#           'the forked road','10,000 feet','psycho','daydream in blue','wires']
# artistList=['muse','lana del rey','daft punk','the neighbourhood','abba','foals','foals','foals','muse','i monster','the neighbourhood']
# for i in range(len(songList)):
#     print(songList[i].upper()+" - "+artistList[i].upper())
#     testSongName = songList[i]
#     testArtistName = artistList[i]
#     testId=spotifySearch(testSongName,testArtistName)
#     spotifySongCharacteristics(testId)

