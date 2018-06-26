import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

# reading csv files to pandas data frames
train_data = pd.DataFrame(pd.read_csv('./input/train.csv'))
test_data = pd.DataFrame(pd.read_csv('./input/test.csv'))
data = [train_data, test_data]

for set in data:
    # checking for missing values
    m_values = set.isnull().sum()
    if m_values.sum()==0:
        print ('No missing values found in dataset.')
    else:
        for i in range(len(m_values)):
            if m_values.data[i] != 0:
                print ('Column {} has {} missing values'.format(m_values.index[i], m_values.data[i]))

# plotting the correlation matrix
corr = train_data.corr()
frame, heatmap = plt.subplots()
# adding correlation data
heatmap.imshow(corr, cmap='inferno')
# setting x,y axes ticks
heatmap.set_xticks(np.arange(train_data.columns.size))
heatmap.set_yticks(np.arange(train_data.columns.size))
# setting x.y axes labels
heatmap.set_xticklabels(train_data.columns)
heatmap.set_yticklabels(train_data.columns)
# rotating x axes labels by 45 degrees for convenience
plt.setp(heatmap.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
# tight layout
frame.tight_layout
# plotting the heat map
plt.show()

# dropping Total Volume Donated (c.c.) column as it shows the strongest linear relationship with Number of Donations
train_data.drop(columns=['Total Volume Donated (c.c.)'], inplace=True)
test_data.drop(columns=['Total Volume Donated (c.c.)'], inplace=True)


# adding 'Days since First Donation' and 'Days since Last Donation' features
train_data = train_data.rename({'Months since Last Donation':'Days since Last Donation'}, axis='columns')
train_data = train_data.rename({'Months since First Donation':'Days since First Donation'}, axis='columns')

train_data['Days since First Donation'] = train_data['Days since First Donation'].apply(lambda x: x*30)
train_data['Days since Last Donation'] = train_data['Days since Last Donation'].apply(lambda x: x*30)

print (train_data.loc(train_data['Days since First Donation'] < 90))
