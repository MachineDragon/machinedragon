"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram= circ_text[i:i + k:1]
            c= circ_text[i+k]
            d= self._st.setdefault(kgram,dict())
            v=d.setdefault(c,0)+1
            d[c]= v
            
    def order(self):
        """
        Returns order k of Markov model.
        """
        
        return self._k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))

        if kgram not in self._st:
                return 0
        return sum(self._st[kgram].values())
        



    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram in self._st and c in self._st[kgram]:
            return self._st[kgram][c]
        else:
            return 0
        

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        prob= []
        total=self.kgram_freq(kgram)
        for c in self._st[kgram].values():
            prob +=[c / total]
        i= stdrandom.discrete(prob)
        return list(self._st[kgram].keys())[i]



    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """
        a= kgram
        for i in range(T - self._k):
            kgram = a[-self._k:]
            a+= self.rand(kgram)
        return a

    def replace_unknown(self, corrupted):


        def argmax(a):
            return a.index(max(a))

       
        
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram_before = corrupted [i - self._k:i]
                kgram_after = corrupted [i + 1:i + 1 + self._k]
                prob = []
                for guess in self._st [kgram_before].keys():
                    context = kgram_before + guess + kgram_after
                    p = 1.0
                    for j in range(self._k + 1):
                        kgram = context [j:j+self._k]
                        char = context [j + self._k]
                        if self.char_freq(kgram,char) == 0:
                            p=0
                            break
                        else:
                            p *= self.char_freq(kgram,char)/self.kgram_freq(kgram)
                    prob.append(p)
                original += list(self._st[kgram_before].keys())[argmax(prob)]
            else:
                original += corrupted[i]
        return original


    




def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
