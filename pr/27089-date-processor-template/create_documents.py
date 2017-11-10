import bz2

def main():
  filename = 'documents.ndjson.bz2'
  num_docs = 10000000
  with bz2.BZ2File(filename, 'wb', compresslevel=9) as output:
    for i in xrange(num_docs):
      output.write('{"my_date": "2017-11-06T12:50:37-0800"}\n')

if __name__ == '__main__':
  main()
