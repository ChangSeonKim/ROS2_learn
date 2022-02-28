def func(a,b):
   5+5 = c


   
   return c

if __name__ == '__main__':
   args = argparse.ArgumentParser()
args.add_argument('-x','--xVal',required=True)
args.add_argument('-y','--yVal',required=False)
argvar = vars(args.parse_args())
   try:
      pass
   except Exception as e:
      pass

