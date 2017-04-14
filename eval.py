import argparse
import sys
import math


def doArgParsing():
  parser = argparse.ArgumentParser()
  parser.add_argument('--score-file', help='File with scores from Lemur',
                      type=str, nargs='?', default=None)
  parser.add_argument('--rank-file', nargs='?', help='Rank File',
                      type=str, default=None)
  parser.add_argument('--test-file', help='test file used for rankin',
                      type=str, default=None)
  parser.add_argument('--NDCG', help='Give K as an argument',
                      type=int, nargs='?', default=None)
  parser.add_argument('--ERR', help='Give K as an argument',
                      type=int, nargs='?', default=None)
  return parser.parse_args()


def getRanks(ranks_file):
  queries = {}
  with open(ranks_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      row = line.split()
      qid = int(row[0])
      uid = int(row[1])
      queries[qid].append(uid)
  return queries


def convertScoresToRanks(score_file):
  queries = {}
  with open(score_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      row = line.split()
      qid = int(row[0])
      uid = int(row[1])
      score = float(row[2])
      if qid not in queries:
        queries[qid] = []
      queries[qid].append((score, uid))

  for qid in queries:
    queries[qid].sort(key=lambda l: l[0], reverse=True)
    for i in range(len(queries[qid])):
      queries[qid][i] = queries[qid][i][1]

  return queries


def addGrade(ranks, test_file):
  queries = {}
  with open(test_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      t = line.split()
      qid = int(t[1].split(':')[1])
      grade = int(t[0])
      if qid not in queries:
        queries[qid] = []
      queries[qid].append(grade)

  for qid in ranks:
    for i in range(len(ranks[qid])):
      ranks[qid][i] = queries[qid][ranks[qid][i]]


def NDCG(rank, k):
  cur = 0.0
  ideal = 0.0
  ideal_rank = sorted(rank, reverse=True)
  for i in range(min(k, len(rank))):
    d = 1.0 / math.log(i + 2, 2)
    cur += (2**rank[i] - 1) * d
    ideal += (2**ideal_rank[i] - 1) * d

  if ideal < 1e-15:
    return 0.0
  return cur / ideal


def ERR(rank, k):
  MX = 16.0
  prob_get_here = 1
  res = 0
  for i in range(min(k, len(rank))):
    prob_yes = (2**rank[i] - 1) / MX
    res += ((prob_yes / (i + 1.0)) * prob_get_here)
    prob_get_here *= (1 - prob_yes)

  return res


def av_rank(ranks, func, k):
  res = 0.0
  for qid in ranks:
    res += func(ranks[qid], k)
  res /= len(ranks)
  return res


if __name__ == '__main__':

  args = doArgParsing()
  ranks = None
  if args.NDCG is None and args.ERR is None:
    print('No eval selected')
    sys.exit()
  if args.rank_file is not None and args.score_file is not None:
    print('only one of score-file or rank-file should be specified')
    sys.exit()
  elif args.rank_file is None and args.score_file is None:
    print('Specify score file or rank file')
    sys.exit()
  elif args.score_file is not None:
    ranks = convertScoresToRanks(args.score_file)
  else:
    ranks = getRanks(args.rank_file)
  assert ranks is not None

  addGrade(ranks, args.test_file)

  if args.NDCG is not None:
    print('NDCG@%d' % (args.NDCG), av_rank(ranks, NDCG, args.NDCG))
  if args.ERR is not None:
    print('ERR@%d' % (args.ERR), av_rank(ranks, ERR, args.NDCG))
