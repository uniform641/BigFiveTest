# 量表来源：Zhang B, Li Y M, Li J, et al. The Big Five Inventory–2 in China: A Comprehensive Psychometric Evaluation in Four Diverse Samples[J]. Assessment, 2021: 10731911211008245.

from pygal.style import Style
import pygal
import cairosvg

question_list = [
"性格外向， 喜欢交际",
"心肠柔软， 有同情心",
"缺乏条理",
"从容， 善于处理压力",
"对艺术没有什么兴趣",
"性格坚定自信， 敢于表达自己的观点",
"为人恭谦， 尊重他人",
"比较懒",
"经历挫折后仍能保持积极心态",
"对许多不同的事物都感兴趣",
"很少觉得兴奋或者特别想要(做)什么",
"常常挑别人的毛病",
"可信赖的， 可靠的",
"喜怒无常， 情绪起伏较多",
"善于创造， 能找到聪明的方法来做事",
"比较安静",
"对他人没有什么同情心",
"做事有计划有条理",
"容易紧张",
"着迷于艺术、 音乐或文学",
"常常处于主导地位， 像个领导一样",
"常与他人意见不和",
"很难开始行动起来去完成一项任务",
"觉得有安全感， 对自己满意",
"不喜欢知识性或者哲学性强的讨论",
"不如别人有活力",
"宽宏大量",
"有时比较没有责任心",
"情绪稳定， 不易生气",
"几乎没有什么创造性",
"有时会害羞， 比较内向",
"乐于助人， 待人无私",
"习惯让事物保持整洁有序",
"时常忧心忡忡， 担心很多事情",
"重视艺术与审美",
"感觉自己很难对他人产生影响",
"有时对人比较粗鲁",
"有效率， 做事有始有终",
"时常觉得悲伤",
"思想深刻",
"精力充沛",
"不相信别人， 怀疑别人的意图",
"可靠的， 总是值得他人信赖",
"能够控制自己的情绪",
"缺乏想象力",
"爱说话， 健谈",
"有时对人冷淡， 漠不关心",
"乱糟糟的， 不爱收拾",
"很少觉得焦虑或者害怕",
"觉得诗歌、 戏剧很无聊",
"更喜欢让别人来领头负责",
"待人谦逊礼让",
"有恒心， 能坚持把事情做完",
"时常觉得郁郁寡欢",
"对抽象的概念和想法没什么兴趣",
"充满热情",
"把人往最好的方面想",
"有时候会做出一些不负责任的行为",
"情绪多变， 容易愤怒",
"有创意， 能想出新点子"
]
question_prefix = "我是一个。。。的人"
score_standard = "1：非常不同意， 2：不太同意， 3：态度中立， 4：比较同意， 5：非常同意"
score_standard_list = ["", "非常不同意", "不太同意", "态度中立", "比较同意", "非常同意"]

# 大五人格维度
# 外向性 (Extraversion): 1, 6, 11R, 16R, 21, 26R, 31R, 36R, 41, 46, 51R, 56
# 宜人性 (Agreeableness): 2, 7, 12R, 17R, 22R, 27, 32, 37R, 42R, 47R, 52, 57
# 尽责性 (Conscientiousness): 3R, 8R, 13, 18, 23R, 28R, 33, 38, 43, 48R, 53, 58R
# 负性情绪/神经质 (Negative Emotionality): 4R, 9R, 14, 19, 24R, 29R, 34, 39, 44R, 49R, 54, 59
# 开放性 (Open-Mindedness): 5R, 10, 15, 20, 25R, 30R, 35, 40, 45R, 50R, 55R, 60
Extraversion_standard = [1, 6, -11, -16, 21, -26, -31, -36, 41, 46, -51, 56]
Agreeableness_standard = [2, 7, -12, -17, -22, 27, 32, -37, -42, -47, 52, 57]
Conscientiousness_standard = [-3, -8, 13, 18, -23, -28, 33, 38, 43, -48, 53, -58]
NegativeEmotionality_standard = [-4, -9, 14, 19, -24, -29, 34, 39, -44, -49, 54, 59]
OpenMindedness_standard = [-5, 10, 15, 20, -25, -30, 35, 40, -45, -50, -55, 60]
extraversion_score = 0
agreeableness_score = 0
conscientiousness_score = 0
negativeEmotionality_score = 0
openMindedness_score = 0

# 大五人格子维度
# 社交 (Sociability): 1, 16R, 31R, 46
# 果断 (Assertiveness): 6, 21, 36R, 51R
# 活力 (Energy Level): 11R, 26R, 41, 56
# 同情 (Compassion): 2, 17R, 32, 47R
# 谦恭 (Respectfulness): 7, 22R, 37R, 52
# 信任 (Trust): 12R, 27, 42R, 57
# 条理 (Organization): 3R, 18, 33, 48R
# 效率 (Productiveness): 8R, 23R, 38, 53
# 负责 (Responsibility): 13, 28R, 43, 58R
# 焦虑 (Anxiety): 4R, 19, 34, 49R
# 抑郁 (Depression): 9R, 24R, 39, 54
# 易变 (Emotional Volatility): 14, 29R, 44R, 59
# 好奇 (Intellectual Curiosity): 10, 25R, 40, 55R
# 审美 (Aesthetic Sensitivity): 5R, 20, 35, 50R
# 想象 (Creative Imagination): 15, 30R, 45R, 60
Social_standard = [1, -16, -31, 46]
Assertiveness_standard = [6, 21, -36, -51]
EnergyLevel_standard = [-11, -26, 41, 56]
Compassion_standard = [2, -17, 32, -47]
Respectfulness_standard = [7, -22, -37, 52]
Trust_standard = [-12, 27, -42, 57]
Organization_standard = [-3, 18, 33, -48]
Productiveness_standard = [-8, -23, 38, 53]
Responsibility_standard = [13, -28, 43, -58]
Anxiety_standard = [-4, 19, 34, -49]
Depression_standard = [-9, -24, 39, 54]
EmotionalVolatility_standard = [14, -29, -44, 59]
IntellectualCuriosity_standard = [10, -25, 40, -55]
AestheticSensitivity_standard = [-5, 20, 35, -50]
CreativeImagination_standard = [15, -30, -45, 60]
social_score = 0
assertiveness_score = 0
energyLevel_score = 0
compassion_score = 0
respectfulness_score = 0
trust_score = 0
organization_score = 0
productiveness_score = 0
responsibility_score = 0
anxiety_score = 0
depression_score = 0
emotionalVolatility_score = 0
intellectualCuriosity_score = 0
aestheticSensitivity_score = 0
creativeImagination_score = 0

answer_list = [0]

if __name__ == '__main__':
    print("大五人格问卷第二版 (BFI-2)")
    print("回答共计60个问题，均关于'", question_prefix, "'")
    print("分值范围：", score_standard)
    print("---------------------------------------------------")
    for index, question in enumerate(question_list):
        print("第("+str(index + 1)+"/60)题：", question)
        answer = input("请输入分值：")
        while 1:
            if answer.isdigit() and int(answer) in range(1, 6):
                answer_list.append(answer)
                print("您的答案是：", score_standard_list[int(answer)])
                print("~~~~~~~~~~~~~~~")
                break
            else:
                answer = input("输入有误，请重新输入：")
    print("---------------------------------------------------")
    for index in Extraversion_standard:
        if index > 0:
            extraversion_score += int(answer_list[index])
        else:
            extraversion_score += 6 - int(answer_list[-index])
    for index in Agreeableness_standard:
        if index > 0:
            agreeableness_score += int(answer_list[index])
        else:
            agreeableness_score += 6 - int(answer_list[-index])
    for index in Conscientiousness_standard:
        if index > 0:
            conscientiousness_score += int(answer_list[index])
        else:
            conscientiousness_score += 6 - int(answer_list[-index])
    for index in NegativeEmotionality_standard:
        if index > 0:
            negativeEmotionality_score += int(answer_list[index])
        else:
            negativeEmotionality_score += 6 - int(answer_list[-index])
    for index in OpenMindedness_standard:
        if index > 0:
            openMindedness_score += int(answer_list[index])
        else:
            openMindedness_score += 6 - int(answer_list[-index])
    print("您的大五人格结果如下：")
    print("外向性(Extraversion)：", extraversion_score / 60 * 100, "%")
    print("宜人性(Agreeableness)：", agreeableness_score / 60 * 100, "%")
    print("尽责性 (Conscientiousness)：", conscientiousness_score / 60 * 100, "%")
    print("负性情绪/神经质 (Negative Emotionality)：", negativeEmotionality_score / 60 * 100, "%")
    print("开放性(Open Mindedness)：", openMindedness_score / 60 * 100, "%")
    style = Style(font_family = 'SimHei')
    main_radar_chart = pygal.Radar(fill=True, range=(0, 60), style=style)
    main_radar_chart.title = '大五人格问卷第二版 (BFI-2) 大五人格结果'
    main_radar_chart.x_labels = ['外向性(Extraversion)', '宜人性(Agreeableness)', '尽责性 (Conscientiousness)', '负性情绪/神经质 (Negative Emotionality)', '开放性(Open Mindedness)']
    main_radar_chart.add('您的大五人格结果', [extraversion_score, agreeableness_score, conscientiousness_score, negativeEmotionality_score, openMindedness_score])
    #main_radar_chart.render_to_png('大五人格结果.png')
    main_radar_chart.render_to_file('大五人格结果.svg')
    print("---------------------------------------------------")
    for index in Social_standard:
        if index > 0:
            social_score += int(answer_list[index])
        else:
            social_score += 6 - int(answer_list[-index])
    for index in Assertiveness_standard:
        if index > 0:
            assertiveness_score += int(answer_list[index])
        else:
            assertiveness_score += 6 - int(answer_list[-index])
    for index in EnergyLevel_standard:
        if index > 0:
            energyLevel_score += int(answer_list[index])
        else:
            energyLevel_score += 6 - int(answer_list[-index])
    for index in Compassion_standard:
        if index > 0:
            compassion_score += int(answer_list[index])
        else:
            compassion_score += 6 - int(answer_list[-index])
    for index in Respectfulness_standard:
        if index > 0:
            respectfulness_score += int(answer_list[index])
        else:
            respectfulness_score += 6 - int(answer_list[-index])
    for index in Trust_standard:
        if index > 0:
            trust_score += int(answer_list[index])
        else:
            trust_score += 6 - int(answer_list[-index])
    for index in Organization_standard:
        if index > 0:
            organization_score += int(answer_list[index])
        else:
            organization_score += 6 - int(answer_list[-index])
    for index in Productiveness_standard:
        if index > 0:
            productiveness_score += int(answer_list[index])
        else:
            productiveness_score += 6 - int(answer_list[-index])
    for index in Responsibility_standard:
        if index > 0:
            responsibility_score += int(answer_list[index])
        else:
            responsibility_score += 6 - int(answer_list[-index])
    for index in Anxiety_standard:
        if index > 0:
            anxiety_score += int(answer_list[index])
        else:
            anxiety_score += 6 - int(answer_list[-index])
    for index in Depression_standard:
        if index > 0:
            depression_score += int(answer_list[index])
        else:
            depression_score += 6 - int(answer_list[-index])
    for index in EmotionalVolatility_standard:
        if index > 0:
            emotionalVolatility_score += int(answer_list[index])
        else:
            emotionalVolatility_score += 6 - int(answer_list[-index])
    for index in IntellectualCuriosity_standard:
        if index > 0:
            intellectualCuriosity_score += int(answer_list[index])
        else:
            intellectualCuriosity_score += 6 - int(answer_list[-index])
    for index in AestheticSensitivity_standard:
        if index > 0:
            aestheticSensitivity_score += int(answer_list[index])
        else:
            aestheticSensitivity_score += 6 - int(answer_list[-index])
    for index in CreativeImagination_standard:
        if index > 0:
            creativeImagination_score += int(answer_list[index])
        else:
            creativeImagination_score += 6 - int(answer_list[-index])
    print("您的大五人格子维度结果如下：")
    print("社交(Sociability)：", social_score / 20 * 100, "%")
    print("果断 (Assertiveness)：", assertiveness_score / 20 * 100, "%")
    print("活力 (Energy Level)：", energyLevel_score / 20 * 100, "%")
    print("同情 (Compassion)：", compassion_score / 20 * 100, "%")
    print("谦恭 (Respectfulness)：", respectfulness_score / 20 * 100, "%")
    print("信任 (Trust)：", trust_score / 20 * 100, "%")
    print("条理 (Organization)：", organization_score / 20 * 100, "%")
    print("效率 (Productiveness)：", productiveness_score / 20 * 100, "%")
    print("负责 (Responsibility)：", responsibility_score / 20 * 100, "%")
    print("焦虑 (Anxiety)：", anxiety_score / 20 * 100, "%")
    print("抑郁 (Depression)：", depression_score / 20 * 100, "%")
    print("易变 (Emotional Volatility)：", emotionalVolatility_score / 20 * 100, "%")
    print("好奇 (Intellectual Curiosity)：", intellectualCuriosity_score / 20 * 100, "%")
    print("审美 (Aesthetic Sensitivity)：", aestheticSensitivity_score / 20 * 100, "%")
    print("想象 (Creative Imagination)：", creativeImagination_score / 20 * 100, "%")
    extend_rader_chart = pygal.Radar(fill=True, range=(0, 20), style=style)
    extend_rader_chart.title = '大五人格问卷第二版 (BFI-2) 大五人格子维度结果'
    extend_rader_chart.x_labels = ['社交(Sociability)', '果断 (Assertiveness)', '活力 (Energy Level)', '同情 (Compassion)', '谦恭 (Respectfulness)', '信任 (Trust)', '条理 (Organization)', '效率 (Productiveness)', '负责 (Responsibility)', '焦虑 (Anxiety)', '抑郁 (Depression)', '易变 (Emotional Volatility)', '好奇 (Intellectual Curiosity)', '审美 (Aesthetic Sensitivity)', '想象 (Creative Imagination)']
    extend_rader_chart.add('您的大五人格子维度结果', [social_score, assertiveness_score, energyLevel_score, compassion_score, respectfulness_score, trust_score, organization_score, productiveness_score, responsibility_score, anxiety_score, depression_score, emotionalVolatility_score, intellectualCuriosity_score, aestheticSensitivity_score, creativeImagination_score])
    #extend_rader_chart.render_to_png('大五人格子维度结果.png')
    extend_rader_chart.render_to_file('大五人格子维度结果.svg')