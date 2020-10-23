
import re
import json
def handle_dialogue_bak(data):

    data_list=data.split("}]},")
    if len(data_list) < 2:
        return "\n"
    speaker_flag=re.match(r'.*\"speaker\":\"(.*)\"', str(data_list[0]), re.M|re.I).group(1)
    flag0=speaker_flag
    qa_list=["A:"]
    for element in data_list[:-1]:
        seg=re.match(r'.*\"onebest\":\"(.*)\",.*', str(element), re.M|re.I).group(1)
        speaker=re.match(r'.*\"speaker\":\"(.*)\"', str(element), re.M|re.I).group(1)

        if speaker == speaker_flag:
            print(qa_list)
            print(qa_list[-1])
            qa_list[-1]=qa_list[-1]+seg
            print(qa_list)
            print(qa_list[-1])
        else:

            if speaker == flag0:
                qa_list.append("A:"+seg)
            else:
                qa_list.append("B:"+seg)
            speaker_flag=speaker
    result = "\n".join(qa_list)
    return result

def handle_dialogue(data):
    if len(data) < 2:
        return "absent"

    speaker_flag=data[0]['speaker']
    flag0=speaker_flag
    qa_seg_list=["A:"]
    qa_word_list=[]
    for ele in data[:-1]:
        seg=ele['onebest']
        speaker=ele['speaker']
        for ele_1 in ele["wordsResultList"]:
            qa_word_list.append(ele_1["wordsName"])


        if speaker == speaker_flag:
            qa_seg_list[-1]=qa_seg_list[-1]+seg
        else:

            if speaker == flag0:
                qa_seg_list.append("A:"+seg)
            else:
                qa_seg_list.append("B:"+seg)
            speaker_flag=speaker


    result_seg = "\n".join(qa_seg_list)
    result_word="*".join(qa_word_list)
    print(result_seg)
    print(result_word)
    return result_seg,qa_word_list

if __name__ == "__main__":
    with open("data/test1.txt","r",encoding='utf-8') as f:
        res=json.load(f)
    res=json.loads(res["data"])
    handle_dialogue(res)






