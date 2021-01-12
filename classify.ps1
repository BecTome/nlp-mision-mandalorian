$model=$args[0]
$lenargs=$args.Count - 1
$paths=$args[1..$lenargs]

python classify.py $model $paths
