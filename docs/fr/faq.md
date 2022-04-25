---
title: Avant-propos, FAQ et éléments de traduction
author: Loïck Bourdois
date: 14 Nov 2021
lang-ref: faq
lang: fr
---

#	Avant-propos
Ce cours porte sur les techniques de représentation et d'apprentissage profond les plus récentes. Il se concentre sur l'apprentissage supervisé, non supervisé et autosupervisté, mais aussi sur les méthodes d’enchâssement, l'apprentissage métrique et les réseaux convolutifs et récurrents. 
Il est illustré d’applications à la vision par ordinateur, la compréhension du langage naturel et la reconnaissance vocale.
Pour suivre ce cours, il est fortement conseillé d’avoir des prérequis en algèbre et d’avoir déjà suivi un cours introductif d'apprentissage machine ou de *data science*. D’après Yann Le Cun, ces cours sont destinés à des personnes de niveau bac+4 ou bac+5.
  
Nous vous invitons à privilégier les vidéos de la [chaine YouTube](https://www.youtube.com/watch?v=0bMe_vCZo30&list=PLLHTzKZzVU9eaEyErdV26ikyolxOsz6mq) (contenu « officiel ») puisque le cours y est donné par le corps enseignant contrairement au site web où il s’agit des notes prises par les étudiants pendant le cours.
Le site web étant des résumés des vidéos, celles-ci comprennent donc généralement des informations supplémentaires par rapport au site. Comme par exemple :
-	des anecdotes sur les différents concepts abordés,
-	des blagues, 
-	la répétition d’un même concept mais sous la forme de différentes formulations permettant ainsi généralement de comprendre une idée si une première formulation n’est pas saisie, 
-	les questions des étudiants qui peuvent être celles que vous ayez vous-même pendant le visionnage,
Notez que si des concepts ne sont toujours pas compris à l’issue de la vidéo, vous avez la possibilité de poser une question en commentaire de la vidéo YouTube, ce que ne permet pas le site web.
-	les références des articles sur lesquels se basent le cours sont présentes sur les diapositives des vidéos alors qu’elles sont absentes du site.  
  
Le site web sert ainsi davantage de résumé des vidéos ou encore de base que vous pouvez réutiliser pour vos notes personnelles que vous prenez pendant le visionnage des vidéos. 
En cas de besoin vous pouvez facilement basculer du site à un moment d’une vidéo donnée en cliquant sur les titres des paragraphes des pages web.



# FAQ
Voici quelques réponses à des questions fréquemment posées :
-	**Est-ce que suivre ce cours permet d’obtenir une certification ?**  
>	Non. Pour proposer une certification, il faudrait pouvoir vous évaluer or le contenu n’a pas été prévu pour (contrairement à un MOOC par exemple).    
>	Cette demande étant fréquente, des réflexions sont menées pour essayer d’en proposer une pour des éditions futures du cours.
-	**Une version plus récente du cours existe. Cette édition 2020 est-elle encore valable ?**  
> Absolument. L’édition 2021 est sensiblement la même que celle de 2020 mais est présentée d’une façon différente : les travaux dirigés sont maintenant abordés du point de vue des modèles à base d’énergie et les cours magistraux ont été légèrement réorganisées. Les invités diffèrent également. Concernant le français, le site web de l’édition 2021 a été traduit mais pas les vidéos (elles ne le seront probablement pas car ce travail est extrêmement chronophage, voir la section 3 ci-dessous). Ainsi nous vous conseillons de commencer avec cette édition 2020 pour le français puis explorer par vous-même par la suite l’édition 2021 au besoin. 
-	**Combien de temps consacrer à ce cours ?**  
> Pour chaque semaine, il y a environ 2h30/3h de contenu vidéo. Avec le temps consacré à la prise de notes et celui pour jouer avec les *notebooks*, une estimation totale de 5h par semaine semble raisonnable. Pour la suite, cela dépend du niveau d'immersion que vous voulez atteindre dans un sujet donné (lire les articles donnés en référence, appliquer ce qui a été vu en classe à vos propres projets, etc.).
-	**Où poser une question à l’issue du visionnage d’une vidéo ?**  
>	Vous pouvez la poser directement (en anglais) dans la section commentaires sous la vidéo YouTube en question, Alfredo se fera un plaisir d’y répondre. Si cette question porte sur un point précis de la vidéo, pensez à indiquer l’horodatage. Vous pouvez le faire également sur le [Discord](https://discord.gg/CthuqsX8Pb) de la classe dédié expressément aux étudiants. Il sert également à coordonner des groupes de visionnage, discuter des devoirs, suggérer des améliorations ou plus généralement pour tout sujet lié au cours.
- **Puis-je utiliser ce cours?**  
> Bien sûr, le cours est placé sous la [Licence internationale Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr).
> Cela signifie que :
> - Vous n'êtes pas autorisé à faire un usage commercial de cette œuvre.
> - Vous devez créditer l'œuvre, intégrer un lien vers la licence et indiquer si des modifications ont été effectuées à l'œuvre. Vous devez indiquer ces informations par tous les moyens raisonnables, sans toutefois suggérer que l'offrant vous soutient ou soutient la façon dont vous avez utilisé son œuvre.
> - Dans le cas où vous effectuez un remix, que vous transformez, ou créez à partir du matériel à partir de l'œuvre originale, vous devez diffuser l'œuvre modifiée dans les mêmes conditions, c'est à dire avec la même licence avec laquelle l'œuvre originale a été diffusée. 
>  
> - Pour le crédit, vous pouvez utiliser le BibTeX suivant :
> @misc{canziani2020nyudlsp20,  
  author = {Canziani, Alfredo and LeCun, Yann},  
  title = {NYU Deep Learning, Spring 2020},  
  howpublished = "\url{https://atcold.github.io/pytorch-Deep-Learning/}",  
  year = {2020},  
  note = "[Online; accessed <today>]"  
}



#	Traduction
Vous trouverez ici les informations concernant les choix de traduction adoptés.

###	Informations de base : 
- Pour le site :  
Tous les textes présents sur ce site sont des notes de cours prises par les étudiants de la *New York University* lors des cours donnés par Yann Le Cun, Alfredo Canziani, Aaron Defazio, Ishan Misra, Mike Lewis et Xavier Bresson.  
Ainsi les textes en anglais ont été rédigés par plus de 130 personnes, ce qui a un impact sur l’homogénéité des textes (certains écrivent au passé, d’autres au présent ; les abréviations utilisées ne sont pas forcément toujours les mêmes ; certains écrivent des phrases courtes, quand d’autres écrivent des phrases pouvant aller jusqu’à 5 ou 6 lignes, etc.).  
La traduction en français qui vous est proposée a été effectuée par une seule personne dans le but d’atténuer les problèmes cités à l’instant et de proposer une traduction homogène.

- Pour les vidéos :  
Afin de fluidifier la traduction et la compréhension, il a été décidé de ne pas retranscrire les mots « parasites » de remplissage et de transition (les « *you know* »,  « *sort of* », « *right* », « *so* », etc.).  
Quand le débit est élevé, une traduction ne reste qu'environ 4 secondes à l'écran. Pour pouvoir retranscrire le plus d'informations possibles dans cet intervalle de temps, nous utilisons des abréviations lorsque cela est possible (« RNNs » au lieu de « réseaux de neurones récurrents » par exemple). Nous privilégions également l'usage de mots courts (par exemple un « car » à la place d’un « parce que »).  
En raison du travail important nécessaire pour effectuer la traduction (1h de travail pour 10min de vidéo et plus généralement plus de 600h de travail pour la traduction complète du cours) il n'a pas été possible d'effectuer une relecture détaillée des traductions vidéos. Ainsi, si vous remarquez des fautes d'orthographe/de conjugaison, fautes de frappes, etc., nous vous invitons à soumettre une PR sur le [répertoire GitHub du site](https://github.com/Atcold/pytorch-Deep-Learning/pulls) en précisant avec un `[FR]` qu’elle concerne la traduction française.


###	Choix de traductions des termes techniques : 

- Choix de traduire les termes anglais en français :

Terme | Traduction | Raisons / Explications
--- | --- |--- | 
Chain rule  | Règle de dérivation des fonctions composées | En pratique usage du terme « règle de la chaîne » dans les sous-titres des vidéos pour gagner de la place.
CNN  | ConvNet | Yann tient particulièrement au respect de cette traduction. Voir notamment la page 202 du livre [*Quand la machine apprend*](https://www.odilejacob.fr/catalogue/sciences/informatique/quand-la-machine-apprend_9782738149312.php).
Downstream tasks  | Tâches en aval | Les tâches de prétexte étant les tâches en amont.
Energy-Based Models  | Modèles à base d’énergie | Traduction pas forcément satisfaisante mais adoptée faute de mieux.
Embedding  | Enchâssement | Reprise de la traduction utilisée page 228 dans le livre *Quand la machine apprend*. Dans la littérature, il est possible de trouver également l'usage du terme « plongement » comme traduction. Parler tout simplement de vectorisation paraîtrait beaucoup plus simple pour faire le lien avec le concept mathématique (on vectorise un mot par exemple).
Forward model | Modèle prédictif |
Graph Neural Networks  | Réseaux de neurones pour graphe | En pratique, pour les sous-titres des vidéos, l'abréviation GNN est privilégiée.
Graph Convolution Networks  | Réseaux convolutifs pour graphe | En pratique, pour les sous-titres des vidéos, l'abréviation GCN est privilégiée.
Manifold  | Variété | Voir [l'article Wikipédia](https://fr.wikipedia.org/wiki/Vari%C3%A9t%C3%A9_(g%C3%A9om%C3%A9trie)).
Nonlinearity function	 | Fonction non linéaire | En français, on utilise également le terme de « fonction d’activation ».
Overfitting  | Surentraînement | Reprise de la traduction utilisée page 155 dans le livre *Quand la machine apprend*.
Regularizer  | Régulariseur | Néologisme préférable à régularisateur.
Sparse  | Epars | Pour l'expression « sparse matrix », nous traduisons « sparse » en « creuse » pour « matrice creuse ». Pour tous les autres cas nous utilisons « épars » ou « éparse » en fonction du genre du mot auquel l'adjectif se rapporte.
Sparsity  | Eparsité | Néologisme basé sur le mot « épars ».
Template Matching  | Template Matching | L'expression « appariement de patrons » comme traduction peut être trouvable sur le site ou dans les vidéos.
Yann LeCun |	Yann Le Cun ou Yann	| L'explication de l'écriture du nom de famille est donnée page 193 du livre *Quand la machine apprend*. Dans les notes en anglais des étudiants, il est possible de trouver « Mr Yann LeCun », « Mr LeCun », « Doctor Yann LeCun », « Professor LeCun », etc. Nous utilisons simplement « Yann ».
 
 - Choix de ne pas traduire les termes anglais en français :  
Nous avons fait le choix de ne pas traduire certains termes anglais pour des raisons pratiques. Par exemple, certains concepts nécessitent 3 ou 4 mots en français là où 1 seul suffit en anglais. Cela pose notamment problème pour les vidéos où le temps d'affichage est limité, d'où la préférence à garder le terme en anglais. Il serait possible d'utiliser des néologismes mais nous avons préféré ne pas en imposer car ne pouvant peut-être pas faire consensus. Sur le site, les mots laissés en anglais sont indiqués en italique. 

Terme | Traduction | Raisons / Explications
--- | --- |--- | 
Dropout | Dropout | Le mot « décimation » serait approprié mais il est déjà utilisé en traitement du signal pour signifier « sous-échantillonnage ».
Finetuning | Finetuning | Le terme « affinage » peut être trouvable dans la littérature. 
One hot | One hot | La notion de « vecteurs de base canonique » pourrait être utilisée mais elle est un peu technique et l'expression est plutôt longue pour traduire à peine 2 mots.  N.D.T : lorsque j'étais étudiant, dans mes cours d'algèbre linéaire, j'utilisais soit « v.b.c » pour « vecteurs de base canonique » ou bien « zérun » (pour un vecteur contenant des 0 et un 1) mais il s'agit d'une convention personnelle que je ne préfère pas imposer.
Pooling | Pooling | Plusieurs traductions envisagées comme agrégation, agglomération, ou coalescence. Garder le terme en anglais est plus simple (un « max-agrégation » n'est pas très élégant par exemple).


En vous souhaitant un bon visionnage ou une bonne lecture !
