from random import randint
import random as rn




class Sample:
    def __init__(self,s,score):
        self.s = s
        self.score = score

class GeneticEvolution:
    def __init__(self,s):
        self.s = s
        #97 122
        self.population = []
        self.mutation_rate = 0.1
        for i in range(100):
            sample = ''
            for i in range(len(s)):
                sample+= chr(int(randint(97,122)))
            self.population.append(Sample(sample,self.fitness(sample)))
    def fitness(self,sample):
        score=0
        for i,j in zip(list(sample),list(self.s)):
            if i==j:
                score+=1
        return score
    def selection(self):
        new_population = []
       
        self.population.sort(key = lambda x: x.score,reverse=True)
        new_population = self.population[:40]
       
        r_sample = rn.sample(self.population[40:],10)
        for i in r_sample:
            new_population.append(i)
        self.population = new_population
    def crossover(self):
        for i in range(100-len(self.population)):
            parents = rn.sample(self.population,2)
            child = ''
            for i,j in zip(list(parents[0].s),list(parents[1].s)):
                if rn.random()<0.5:
                    child+=i
                else:
                    child+=j
            self.population.append(Sample(child,self.fitness(child)))
           
    def mutation(self):
        new_population = []
       
        for sample in self.population:
            mutated = ''
            for i in sample.s:
                if rn.random()<self.mutation_rate:
                    mutated += chr(int(randint(97,122)))
                else:
                    mutated += i
       
            new_population.append(Sample(mutated,self.fitness(mutated)))
        self.population = new_population
   
    def evolution(self):
        generation = 0
        while True:
            generation+=1
            print(generation)
            self.selection()
            #condition
            if self.population[0].score==self.fitness(self.s):
                print(self.population[0].s,self.population[0].score)
                return self.population[0]
            self.crossover()
            self.mutation()
            if generation>1000:
                return None
           
           
   
     
     
       
g = GeneticEvolution('hel')
g.evolution()
def brute_force(s):
    count = 0
    while True:
        e = ''
        for i in range(len(s)):
            e+=chr(int(randint(97,122)))
        if e==s:
            return count
        print(e)
        if count>10000:
            return -1
        count+=1
