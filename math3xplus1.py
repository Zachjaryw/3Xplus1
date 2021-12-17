import streamlit as st
import pandas as pd
pd.set_option('display.max_columns', None)

st.title("3x+1 Tester")

def test(startingValue):
  endValue = 1
  values = []
  value = startingValue
  values.append(value)
  while value != endValue:
    if value % 2 == 0: #Even
      value = value/2
    elif value % 2 == 1: #Odd
      value = value*3 + 1
    values.append(int(value))
  return values

def singleValue(startingValue):
  values = test(startingValue)
  st.text(values)
  st.text(f'For {startingValue}, it took {len(values)} runs to return to 1.')
  data = pd.DataFrame({"Values":values})
  st.line_chart(data)
  return values


def multipleTests(howMany):
  data = {}
  for i in range(howMany):
    collect = test(i+1)
    data[f'{i+1}'] = [collect,len(collect),max(collect)]
  toshow = pd.DataFrame(data).T
  show = pd.DataFrame(data)[1:3].T
  toshow.columns = ['List of Runs','# of Runs','Maximum Value']
  show.columns = ['# of Runs','Maximum Value']
  st.dataframe(show)
  st.text(f"\nThe test with the most runs was {toshow['# of Runs'].to_list().index(max(toshow['# of Runs']))+1} with {max(toshow['# of Runs'])}")
  graph = st.checkbox('To see graph of all tests, check the box')
  graph = int(graph)
  if graph == 0:
    pass
  elif graph == 1:
    st.line_chart(toshow['# of Runs'])
  return toshow

def run():
  howMany = st.text_input('How many values would you like to test up to?','10')
  howMany = int(howMany)
  toshow = multipleTests(howMany)
  st.text("\n")
  st.markdown(f"Enter a value up to {howMany} to see a single test:")
  selection = st.text_input(f"\nEnter Value Below",toshow['# of Runs'].to_list().index(max(toshow['# of Runs']))+1)
  selection = int(selection)
  if selection == 0:
    pass
  elif selection > 0 and selection <= howMany:
    singleValue(selection)
  else:
    st.text('Invalid Input: Please try again')

run()
