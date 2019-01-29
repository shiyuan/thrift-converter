rm -rf gen-py
thrift --gen py demo.thrift
python demo.py
