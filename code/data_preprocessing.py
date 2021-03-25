import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False


def main():
    cancer_data = pd.read_csv('../data/1979_2017.csv', error_bad_lines=False)
    cancer_data = cancer_data.drop(['WHO2000', 'Count', 'AgeAvg', 'AgeMed'], axis=1)
    cancer_list = cancer_data['Cancer'].unique()
    gender = cancer_data['Gender'].unique()
    male(cancer_data, cancer_list, gender)
    female(cancer_data, cancer_list, gender)


def male(cancer_data, cancer_list, gender):
    index = 0
    for cancer in cancer_list:
        TT = cancer_data.loc[(cancer_data['Gender'] == gender[1]) &
                             (cancer_data['Cancer'] == cancer)].groupby(['Country']).mean()
        TT = TT.drop(['Year'], axis=1)
        TT.rename(columns={'IncidenceRate': cancer}, inplace=True)
        if (index == 0):
            result = TT
        else:
            result = result.join(TT)
        index = index + 1
    result = result.fillna(0)
    result = result.drop(['全癌症', '男性乳房', '攝護腺', '睪丸', '其他男性生殖器官', ], axis=1)
    colormap = plt.cm.rainbow
    plt.figure(figsize=(40, 40))
    plt.title('男性癌症關聯分析', y=1.05, size=32)
    sns.heatmap(result.astype(float).corr(), linewidths=0.1, vmax=1.0,
                square=True, cmap=colormap, linecolor='white', annot=True)
    # plt.show()
    # plt.savefig('../img/male_cancer_cor.png')


def female(cancer_data, cancer_list, gender):
    index = 0
    for cancer in cancer_list:
        TT = cancer_data.loc[(cancer_data['Gender'] == gender[2]) &
                             (cancer_data['Cancer'] == cancer)].groupby(['Country']).mean()
        TT = TT.drop(['Year'], axis=1)
        TT.rename(columns={'IncidenceRate': cancer}, inplace=True)
        if (index == 0):
            result = TT
        else:
            result = result.join(TT)
        index = index + 1

    result = result.fillna(0)
    result = result.drop(['全癌症', '女性乳房', '子宮', '子宮頸', '子宮體', '卵巢、輸卵管及寬韌帶', '其他女性生殖器官', ], axis=1)

    colormap = plt.cm.rainbow
    plt.figure(figsize=(40, 40))
    plt.title('女性癌症關聯分析', y=1.05, size=32)
    sns.heatmap(result.astype(float).corr(), linewidths=0.1, vmax=1.0,
                square=True, cmap=colormap, linecolor='white', annot=True)
    # plt.show()
    # plt.savefig('../img/female_cancer_cor.png')


if __name__ == '__main__':
    main()
