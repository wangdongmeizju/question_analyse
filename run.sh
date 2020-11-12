#!/usr/bin/env bash
cd speech_recognize
project_path="/Users/jingmo/PycharmProjects/question_analyse"
python speech_recognize_xunfei.py --input=$project_path"/信息中心录音数据/20201014" \
                                  --output=$project_path"/data/20201014.txt"         \
                                  --handle_ok_file=$project_path"/data/speech_handle_ok"
cd ..//bert-utils
#讲对话文本向量化
python dialogues_vectos_wang.py
#分类
python kmeans.py