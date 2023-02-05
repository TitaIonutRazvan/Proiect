import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importarea datelor
data = pd.read_csv("data.csv")

#stergerea coloanelor Timestamp si What is your CGPA?
data = data.drop(columns=["Timestamp","What is your CGPA?"])

#calcularea procentajului de persoane care au depresie
depression_percentage = data["Do you have Depression?"].value_counts(normalize=True)[1] * 100
print("Procentajul de persoane care au depresie: {:.2f}%".format(depression_percentage))

#gruparea datelor dupa gen si an de studiu
grouped_data = data.groupby(["Choose your gender", "Age"])

#calcularea mediei varstei pentru fiecare grup
mean_age = grouped_data["Age"].mean()
print("Media varstei = {}".format(mean_age))



#afisam detalii generale (media, mediana, etc) pentru coloana "Age":
print(data['Age'].describe())

#gruparea datelor dupa gen si starea civila
grouped_data_2 = data.groupby(["Choose your gender", "Marital status"])

#calcularea numarului de persoane cu anxietate pentru fiecare grup
anxiety_count = grouped_data_2["Do you have Anxiety?"].sum()
print("Numarul persoanelor care au anxietate = {}".format(anxiety_count))


# metodata de agregare - > grupam dupa coloanele "Your current year of Study", "Did you seek any specialist for a treatment?"
treatment_data = data.groupby(["Your current year of Study", "Did you seek any specialist for a treatment?"])
#calcularea procentajului de persoane care au cautat un specialist pentru fiecare grup
treatment_percentage = treatment_data.size().groupby(level=0).apply(lambda x: x / x.sum() * 100)

print("Procentajul de persoane care au cautat un specialist pentru fiecare grup = {}".format(treatment_percentage))

# pivotarea datelor pentru a crea o noua tabel cu coloana 'Your current year of Study' si randurile ca 'Choose your gender' cu valorile ca numar de persoane care au anxietate
pivot_table = data.pivot_table(values='Do you have Anxiety?', index='Choose your gender', columns='Your current year of Study', aggfunc='sum', fill_value=0)
print(pivot_table)


#Pivotarea datelor dupa coloana "Choose your gender" si "Marital status"
pivot = data.pivot_table(index='Choose your gender', columns='Marital status', values='Age')
print(pivot)

#vizualizarea datelor într-un histogram pentru coloana "Age"

data['Age'].plot.hist()
plt.show()
#crearea unui grafic de tip "bar" pentru a vizualiza media varstei pentru fiecare grup
mean_age.plot(kind="bar", grid=True, label = "Age")
plt.xlabel("Gender and Year of Study")
plt.ylabel("Mean")
plt.title("Mean Age by Gender and Year of Study")
plt.legend()

#afisam graficul
plt.show()


#Vizualizarea unei heatmap pentru coloanele Choose your gender si Age :
sns.heatmap(data[['Choose your gender', 'Age']].corr(), annot=True)
plt.show()