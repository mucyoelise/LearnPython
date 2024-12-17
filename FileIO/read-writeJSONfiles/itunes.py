import json
import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit('Usage: python <file_name>.py band_name(Try: weezer)')

    # Requesting to itune API to get the 5 songs of weezer so as to write them to the file
    response = requests.get('https://itunes.apple.com/search?entity=song&limit=5&term='+sys.argv[1])

    # Converting Json response into python dictionary
    response_dict = response.json()

    # Sending data to the file named weezer_songs.json in Json form.
    write_jsonfile(response_dict) 

    # Printing data sent to the file named weezer_songs.json in the clear way to be readable.
    print(json.dumps(response_dict, indent=4))

    # Printing the 5 songs of weezer band we get from itune API:
    print('\n********************* The 5 songs of weezer band are: ****************************')
    for items in response_dict['results']:
        print(f'{items['trackName']}')
    print()

def write_jsonfile(dictionary):
    # Opening json file and writting to it using dump funtion in the json module.
    with open('weezer_songs.json', 'w') as aFile:
        json.dump(dictionary, aFile)


if __name__ == '__main__':
    main()