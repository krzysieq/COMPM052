#!/bin/bash
for a in `seq 1 5`; do
	for b in `seq 0 8`; do
		echo "Iteration number $a $b"
		java -jar ./RankLib.jar -train Fold$a/train.txt -test Fold$a/test.txt -validate Fold$a/vali.txt -ranker $a -metric2t NDCG@10 -metric2T ERR@10 -save $a_mymodel$b.txt
	done
done
