# download the fall dataset.

dir_names=("489" "569" "581" "722" "731" "758" "786" "807" "832" "925" "1176" "1219" "1260" "1301" "1373" "1378" "1392" "1790" "1843" "1954" "2123")
# wget https://falldataset.com/data/489.tar.gz
# wait

# wget https://falldataset.com/data/489.tar.gz
# wait

# wget https://falldataset.com/data/489.tar.gz
# wait

# wget https://falldataset.com/data/489.tar.gz
# wait

# wget https://falldataset.com/data/489.tar.gz
# wait
prefix="https://falldataset.com/data/"
dataset="dataset/"
for i in {0..20}  
    do 
        # echo ${dir_names[$i]}
        url=$prefix${dir_names[$i]}'/'${dir_names[$i]}'.tar.gz'
        wget -O ${dataset}${dir_names[$i]}'.tar.gz' $url 

    done





