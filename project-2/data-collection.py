import requests
import hashlib
from pathlib import Path  
from boilerpy3 import extractors
from requests import ReadTimeout, ConnectionError

# A dictionary to hold hash keys to uri mappings
uri_keys = {}

extractor = extractors.ArticleExtractor()
i = 0
with open('uri-list.txt') as uri_file:
    for line in uri_file:
        clean_line = line.strip()
        try:
            if i == 500:
                break
            # Get raw html
            response = requests.get(clean_line, timeout=5)
            t = response.text
            
            # Create hash from uri 
            m = hashlib.md5()
            m.update(line.encode(encoding="utf-8"))
            key = m.hexdigest()
            uri_keys[key] = clean_line
        
            # Save raw html
            raw_file_name = "./raw/{}.txt".format(key)
            raw = Path(raw_file_name)
            raw.write_text(t)
            
            # Save processed html
            # If content = 0 bytes, skip. 
            content = extractor.get_content(response.text)
            processed_file_name = "./processed/{}.txt".format(key)
            processed = Path(processed_file_name)
            processed.write_text(content)

            ++i
        except ReadTimeout:
            print("ReadTimeout error")
        except ConnectionError:
            print("A connection error occurred")
        except TimeoutError:
            print("A general timeout error occured")
        except Exception as e:
            print(f"An unexpected error occurered: {e}")


with open("key_uri.txt", 'w') as f:  
    for key, value in uri_keys.items():  
        f.write('%s.txt,%s\n' % (key, value))
