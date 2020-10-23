# question_analyse

运行 run.sh脚本 可以得到语音的文本对话,和切词结果
sh run.sh
cd bert-utils

运行将文档向量化
python dialogues_vectors_wang.py
进行分类
python kmeans.py
结果保存在 data/days_vector_dict_seg_20 文档保存在 days_vector_dict_dayu30