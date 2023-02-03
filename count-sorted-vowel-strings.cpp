class Solution {
public:
   int contador(int i, int n, string &vogais){

   		if(n==0) return 1; // se a string de tamanho n é formada
   		if(i>=5) return 0; // se i excede o tamanho das vogais

   		int pegar, naoPegar;
   		pegar= contador(i, n-1, vogais);
   		naoPegar= contador(i+1, n, vogais);

   		return pegar + naoPegar;
   }

   int countdorVowelStrings(int n) {
   	 string vogais= "aeiou"; // todas vogais ordenadas lexograficamente 
   	 return contador(0, n, vowels);
   }
};