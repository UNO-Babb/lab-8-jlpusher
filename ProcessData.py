#ProcessData.py
#Name: Jessica Pusher
#Date: 5.11.25
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  outFile.write("Last Name" + "," + "First Name" + "," + "UserID" + "," + "Major-Year" + "\n")

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]
    student_id = makeID(first, last, idNum)
    MajorYear = makeMajorYear(major, year)
    output = last + "," + first + "," + student_id + "," + MajorYear + "\n"
    outFile.write(output)
    #print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  while len(last) < 5:
    last = last + "x"
  id = first[0] + last + idNum[-3:]
  
  return id

def makeMajorYear(major, year):
  if year == "Freshman":
    YR = "FR"
  elif year == "Sophomore":
    YR = "SO"
  elif year == "Junior":
    YR = "JR"
  elif year == "Senior":
    YR = "SR"
  MajorYr = major[0:3] + "-" + YR

  return MajorYr 

if __name__ == '__main__':
  main()
