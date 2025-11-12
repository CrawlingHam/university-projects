from string import punctuation as punctuations

def text_processing(text: str) -> tuple[str, list[str]]:
    chars = list(text)
    prev_was_space = False 
    current_hashtag = [] 
    result_chars = []
    in_tag = False 
    hashtags = []
    i = 0
    
    while i < len(chars):
        char = chars[i]
        char_code = ord(char)
        
        is_printable = 32 <= char_code <= 126
        
        if not is_printable:
            i += 1
            continue
        
        if char == '@':
            in_tag = True
            i += 1
            while i < len(chars) and chars[i] != ' ' and chars[i] not in punctuations:
                i += 1
            in_tag = False
            continue
        
        if in_tag:
            i += 1
            continue
        
        if char == '#':
            current_hashtag = []
            i += 1
            while i < len(chars):
                next_char = chars[i]
                next_code = ord(next_char) if i < len(chars) else 0
                
                if next_char == ' ' or next_char in punctuations:
                    break
                
                if not (32 <= next_code <= 126):
                    i += 1
                    continue
                
                current_hashtag.append(next_char)
                i += 1
            
            if current_hashtag:
                hashtag_word = "".join(current_hashtag)
                hashtags.append(hashtag_word)
                for c in current_hashtag:
                    result_chars.append(c)
                    prev_was_space = False
            continue
        
        if char in punctuations:
            prev_is_letter = False
            next_is_letter = False
            
            if result_chars and len(result_chars) > 0:
                last_char = result_chars[-1]
                prev_is_letter = ('a' <= last_char <= 'z') or ('A' <= last_char <= 'Z')
            
            if i + 1 < len(chars):
                next_char = chars[i + 1]
                next_is_letter = ('a' <= next_char <= 'z') or ('A' <= next_char <= 'Z')
            
            if prev_is_letter and next_is_letter:
                i += 1
                continue
            
            # replace with space
            if not prev_was_space:
                result_chars.append(' ')
                prev_was_space = True
            i += 1
            continue
        
        if char == ' ':
            if not prev_was_space:
                result_chars.append(' ')
                prev_was_space = True
            i += 1
            continue
    
        result_chars.append(char)
        prev_was_space = False
        i += 1
    
    processed_text = "".join(result_chars).strip()
    
    return processed_text, hashtags

if __name__ == "__main__":
    text = "@user @user thanks for #lyft credit i can't use cause they don't offer wheelchair vans in pdx. #disapointed #getthanked"
    processed_text, hashtags = text_processing(text)
    
    print(f"Processed Text: {processed_text}")
    print(f"Hashtags: {hashtags}")

    isProcessedTextCorrect = processed_text == "thanks for lyft credit i cant use cause they dont offer wheelchair vans in pdx disapointed getthanked"
    isHashtagsCorrect = hashtags == ["lyft", "disapointed", "getthanked"]
    print(f"Is Correct for Processed Text: {isProcessedTextCorrect}")
    print(f"Is Correct for Hashtags: {isHashtagsCorrect}")