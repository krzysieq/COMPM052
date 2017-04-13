# COMPM052
Information Retrieval and Data Mining Project

## Microsoft Learning to Rank Datasets
[Homepage](https://www.microsoft.com/en-us/research/project/mslr/)

Direct download links:
* [10k](https://8kmjpq-dm2306.files.1drv.com/y3mI4VdnSMvRrwGXll96CpqRBs1CUaJv9OKDRRBr-6qo283LSzrDhya9cs-iFEU91h1KBOm6TFfUQoRi21MXgFO4PtwsjBeA4R-3RVmdRwWPnRHC45aLKhvDZVXrteuN4JcFYZsMEKTZ-yMXXXH3LdYhYELUqtZvqEZjoGcV_XzjbY/MSLR-WEB10K.zip)
* [30k](https://8kkkbg-dm2306.files.1drv.com/y3mj9yKPdOEK3bQVhfNK78Dy_x50nqsPjfcY5u5HNopc-wZIYMFQ5f7YL_dXwVPTtnFTPRN51-prx9--meOmH_oWqjFD8ImbNTC68XWvJhEknmGTra-muR4xlXRfsvwTK-SBbPmjKU0S6TCRShz02eczqam4I-YHYm7N_EhLQYtGhA/MSLR-WEB30K.zip)

## RankLib
* [RankLib-2.1-patched.jar](https://netcologne.dl.sourceforge.net/project/lemur/lemur/RankLib-2.1/RankLib-2.1-patched.jar)
* [Documentation](https://sourceforge.net/p/lemur/wiki/RankLib%20How%20to%20use/)

## Relevant papers
* [ES-Rank](https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwigpcrQtqHTAhUoAcAKHXQzBTkQFggoMAA&url=http%3A%2F%2Fwww.cs.nott.ac.uk%2F~psxoi%2Fdls_sac2017.pdf&usg=AFQjCNHk_zNtrA39aQJZrApPzQ-m_4GkUg&sig2=0RyYOc3LFMwOxEtE70aqig&bvm=bv.152180690,d.d2s): Runs most relevant algorithm on the MSLR-10K set and a few others. Wouldn't cite it that aggresively, as it beats my results on RankNet with the default values of RankLib. My suspicion is that this is due to the 100 epochs, for which we don't have enough time.
* [RankNet-LambdaRank-LambdaMart](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf): Tries to explain the three algorithms and how they build upon eachother. Not very useful for me, because there's no practical info.
* [RankLib](http://icml.cc/2015/wp-content/uploads/2015/06/icml_ranking.pdf): The paper where they introduce RankNet. They mention some parameter values there + implementation details. Something useful that we can try (and probably get some marks for) is modify the Lemur Project code. In this paper, they mention that after each epoch, if it produces worse results thanthe previous one, they halve the Learning Rate. I looked into the Lemur library code and it seems that they actually have this behavior commented out - we can add it and see how it changes the behaviour of our library.
* [ERR@T] (http://olivier.chapelle.cc/pub/err.pdf): Explains the ERR@T metric and why it is good for evaluating ranking algorothms. 
