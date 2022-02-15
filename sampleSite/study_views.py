from django.shortcuts import render


def study(request):
    # クラス宣言
    user_data1 = {
        'user_id': 's20a2005',
        'name': '稲岡天駿',
        'Science': 50,
        'Mathematics': 80,
        'Physics': 20,
        'Design': 40
    }
    user_data2 = {
        'user_id': 's20a1061',
        'name': '西本光兵',
        'Science': 100,
        'Mathematics': 40,
        'Physics': 20,
        'Design': 90
    }
    user_data3 = {
        'user_id': 's20a2035',
        'name': '佐々木海汰',
        'Science': 50,
        'Mathematics': 30,
        'Physics': 80,
        'Design': 10
    }

    # クラスを宣言
    my_class = MyClass()

    my_class.add_user_data(user=user_data1)
    my_class.add_user_data(user=user_data2)
    my_class.add_user_data(user=user_data3)

    # 合計
    print(my_class.get_user_summary(user_id='s20a2005'))
    # 各教科の平均点
    print(my_class.get_user_average(user_id='s20a2005'))

    print('Design     : '+str(my_class.is_passed(user_id='s20a2005', subject='Design')))
    print('Physics    : '+str(my_class.is_passed(user_id='s20a2005', subject='Physics')))

    print('Physics    : '+str(my_class.get_subject_average(subject='Physics')))
    print('Mathematics: '+str(my_class.get_subject_average(subject='Mathematics')))

    return render(request, 'study.html', {
        "user_id1": "s20a2005",
        "user1": "稲岡天駿",
        "summary1": my_class.get_user_summary("s20a2005"),
        "average1": my_class.get_user_average("s20a2005"),
        'Science1': my_class.is_passed(user_id='s20a2005', subject='Science'),
        'Mathematics1': my_class.is_passed(user_id='s20a2005', subject='Mathematics'),
        'Physics1': my_class.is_passed(user_id='s20a2005', subject='Physics'),
        'Design1': my_class.is_passed(user_id='s20a2005', subject='Design'),

        "user_id2": "s20a1061",
        "user2": "西本光兵",
        "summary2": my_class.get_user_summary("s20a1061"),
        "average2": my_class.get_user_average("s20a1061"),
        'Science2': my_class.is_passed(user_id='s20a1061', subject='Science'),
        'Mathematics2': my_class.is_passed(user_id='s20a1061', subject='Mathematics'),
        'Physics2': my_class.is_passed(user_id='s20a1061', subject='Physics'),
        'Design2': my_class.is_passed(user_id='s20a1061', subject='Design'),

        "user_id3": "s20a2035",
        "user3": "佐々木海汰",
        "summary3": my_class.get_user_summary("s20a2035"),
        "average3": my_class.get_user_average("s20a2035"),
        'Science3': my_class.is_passed(user_id='s20a2035', subject='Science'),
        'Mathematics3': my_class.is_passed(user_id='s20a2035', subject='Mathematics'),
        'Physics3': my_class.is_passed(user_id='s20a2035', subject='Physics'),
        'Design3': my_class.is_passed(user_id='s20a2035', subject='Design')
    })


class MyClass:
    # コンストラクタ
    def __init__(self):
        self.users = []

    def add_user_data(self, user):
        self.users.append(user)
        print(self.users)

    # 全教科の合計を計算
    def get_user_summary(self, user_id):
        # コードを途中で改行したいときは「\」を入れる
        for user in self.users:
            if user['user_id'] == user_id:
                return user['Science']\
                    + user['Mathematics']\
                    + user['Physics']\
                    + user['Design']

    # 全教科の平均点を計算
    def get_user_average(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return (user['Science']
                        + user['Mathematics']
                        + user['Physics']
                        + user['Design'])/4

    # ユーザーの各教科の合格・不合格を判定
    def is_passed(self, user_id, subject):
        for user in self.users:
            if user['user_id'] == user_id:
                if user[subject] >= 50:
                    return True
                else:
                    return False

    # 各教科の平均点
    def get_subject_average(self, subject):
        sum = 0
        for user in self.users:
            sum += user[subject]
        return sum/3


def str_sample():
    # 標準出力へ表示
    print("あああああ")
    # 文字列(ダブルクウォート,シングルクウォートどっちでもいい)
    str1 = "あいうえお "+"かきくけこ "
    print(str1)
    print(str1[0])  # 1文字だけ取り出す
    print(str1[0:4])  # 範囲で取り出したいとき
    print(str1*3)  # 文字列の掛け算もできる
    
    """
    str2 = "さしすせそ"
    # sprintfのようなことも簡単
    print('%s の次は %s' % (str1, str2))
    print('{0} の次は {1}' .format(str1, str2))
    """
    # replaceもありますよ
    print(str1.replace('あいうえお', 'たちつてと'))

    str3 = "cLouD study!"
    print(str3.upper())  # 全部大文字に！
    print(str3.lower())  # 全部小文字に！
    print(str3.count('u')+str3.count('c'))  # 何文字登録するか教えてくれる

    print(10 + 20 * 3 / 4)  # 割り算の時は少数点を表示する
