import json

ideal_dict = {'timestamp': int, 'referer': str, 'location': str, 'remoteHost': str, 'partyId': str,
        'sessionId': str, 'pageViewId': str, 'eventType': str, 'item_id': str, 'item_price': int,
       'item_url': str, 'basket_price': str, 'detectedDuplicate': bool, 'detectedCorruption': bool,
       'firstInSession': bool, 'userAgentName': str}

with open('data.json', encoding='utf8') as f:
    dict_list = json.load(f)

def check_dict(dict):

    answer = "  Пройденные тесты: "
    temp_dict = dict

    keys_error = temp_dict.keys() <= ideal_dict.keys()

    timestamp_error = temp_dict['timestamp']
    referer_error = temp_dict['referer']
    location_error = temp_dict['location']
    remoteHost_error = temp_dict['remoteHost']
    partyId_error = temp_dict['partyId']
    sessionId_error = temp_dict['sessionId']
    pageViewId_error = temp_dict['pageViewId']
    eventType_error = temp_dict['eventType']
    item_id_error = temp_dict['item_id']
    item_price_error = temp_dict['item_price']
    item_url_error = temp_dict['item_url']
    basket_price_error = temp_dict['basket_price']
    detectedDuplicate_error = temp_dict['detectedDuplicate']
    detectedCorruption_error = temp_dict['detectedCorruption']
    firstInSession_error = temp_dict['firstInSession']
    userAgentName_error = temp_dict['userAgentName']

    if isinstance(timestamp_error, int):
        answer +="timestamp_pass"
    else:
        answer +="timestamp_error"

    if referer_error.startswith('http://') or referer_error.startswith('https://'):
        answer +=" referer_pass"
    else:
        answer +=" referer_error"

    if location_error.startswith('http://') or location_error.startswith('https://'):
        answer +=" location_pass"
    else:
        answer +=" location_error"

    if isinstance(remoteHost_error, str):
        answer +=" remoteHost_pass"
    else:
        answer +=" remoteHost_error"

    if isinstance(partyId_error, str):
        answer += " partyId_pass"
    else:
        answer += " partyId_error"

    if isinstance(sessionId_error, str):
        answer += " sessionId_pass"
    else:
        answer += " sessionId_error"

    if eventType_error == "itemBuyEvent" or eventType_error == "itemViewEvent":
        answer += " eventType_pass"
    else:
        answer += " eventType_error"

    if isinstance(item_id_error, str):
        answer += " item_id_pass"
    else:
        answer += " item_id_error"

    if isinstance(item_price_error, int):
        answer += " item_price_pass"
    else:
        answer += " item_price_error"

    if item_url_error.startswith('http://') or item_url_error.startswith('https://'):
        answer += " item_url_pass"
    else:
        answer += " item_url_error"

    if isinstance(basket_price_error, str):
        answer += " basket_price_pass"
    else:
        answer += " basket_price_error"

    if isinstance(detectedDuplicate_error, bool):
        answer += " detectedDuplicate_pass"
    else:
        answer += " detectedDuplicate_error"

    if isinstance(detectedCorruption_error, bool):
        answer += " detectedCorruption_pass"
    else:
        answer += " detectedCorruption_error"

    if isinstance(firstInSession_error, bool):
        answer += " firstInSession_pass"
    else:
        answer += " firstInSession_error"

    if isinstance(userAgentName_error, str):
        answer += " userAgentName_pass"
    else:
        answer += " userAgentName_error"

    answer_count = answer.count("error")
    answerr = answer

    if keys_error == False:
        extra_keys = temp_dict.keys() - ideal_dict.keys()
        print("Лишние ключи " + str(extra_keys) + " Общее количество ошибок " + str(answer_count) + answerr)
    else:
        print("Общее количество ошибок " + str(answer_count) + answerr)



i = 0

while i != len(dict_list):
    check_dict(dict_list[i])
    i += 1

