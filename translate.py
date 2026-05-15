import os
import glob

replacements = {
    'lang="pt-BR"': 'lang="fr"',
    '<title>Oferta Exclusiva</title>': '<title>Offre Exclusive</title>',
    "Pedido quase concluído...": "Commande presque terminée...",
    "Pedido Quase Concluído…": "Commande Presque Terminée...",
    "ESPERE! Seu pedido ainda não está completo...": "ATTENDEZ ! Votre commande n'est pas encore terminée...",
    "Obtenha o <span style=\"font-weight: 400;\">Audiobook</span>": "Obtenez le <span style=\"font-weight: 400;\">Livre Audio</span>",
    "Receba 3 Bônus Adicionais": "Recevez 3 Bonus Supplémentaires",
    "GRÁTIS!": "GRATUITEMENT !",
    "**Oferta Especial Apenas Para Novos Membros**": "**Offre Spéciale Uniquement Pour Les Nouveaux Membres**",
    "Antes de finalizar seu pedido, tenho uma pequena pergunta para você...": "Avant de finaliser votre commande, j'ai une petite question pour vous...",
    "Você já garantiu nosso guia completo que mostra exatamente como controlar sua alimentação": "Vous avez déjà obtenu notre guide complet qui vous montre exactement comment contrôler votre alimentation",
    ", sem abrir mão das comidas que ama.": ", sans renoncer aux aliments que vous aimez.",
    " depois dos 60": " après 60 ans",
    "Mas e se você pudesse absorver tudo com mais facilidade? E se, literalmente, pudesse <em>escutar</em> o guia onde quer que vá, sem precisar forçar a vista ou parar a sua rotina?": "Mais et si vous pouviez tout absorber plus facilement ? Et si vous pouviez littéralement <em>écouter</em> le guide où que vous alliez, sans avoir à forcer vos yeux ou à interrompre votre routine ?",
    "Agora mesmo, você tem a oportunidade exclusiva de aprimorar o seu pedido e obter a versão completa em <strong>Audiobook da": "En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en <strong>Livre audio de",
    "Em vez de ter que encontrar um momento calmo para sentar e ler, basta dar 'play' e começar imediatamente a absorver essas orientações transformadoras. Seja relaxando na poltrona, numa caminhada suave ou lidando com os afazeres da casa...": "Au lieu de devoir trouver un moment de calme pour vous asseoir et lire, il vous suffit d'appuyer sur « lecture » et de commencer immédiatement à absorber ces directives transformatrices. Que vous vous détendiez dans votre fauteuil, que vous fassiez une douce promenade ou que vous vous occupiez des tâches ménagères...",
    "Todo o conteúdo gravado com uma narração profissional e agradável, para você adotar o melhor estilo de vida saudável sem nenhum esforço.": "Tout le contenu est enregistré avec une narration professionnelle et agréable, afin que vous puissiez adopter le meilleur mode de vie sain sans aucun effort.",
    "✓ 100% Adaptado para Iniciantes & Desenvolvido para a Terceira Idade": "✓ 100% Adapté aux Débutants & Conçu pour les Seniors",
    "Veja o que você leva por apenas 29€ hoje:": "Découvrez ce que vous obtenez pour seulement 29€ aujourd'hui :",
    "Ouça em qualquer lugar, a qualquer momento. Perfeito para descansar os olhos e absorver o conhecimento sem estresse.": "Écoutez n'importe où, n'importe quand. Parfait pour reposer vos yeux et absorber les connaissances sans stress.",
    "Bônus nº 1: Comunidade privada (Valor 97€)": "Bonus n° 1 : Communauté privée (Valeur 97€)",
    "Você não está sozinho(a). Tenha acesso rápido para trocar experiências com quem tem objetivos parecidos aos seus.": "Vous n'êtes pas seul(e). Bénéficiez d'un accès rapide pour échanger vos expériences avec d'autres personnes partageant les mêmes objectifs.",
    "Bônus nº 2: Áudios de Receitas Guiadas (Valor 147€)": "Bonus n° 2 : Audios de Recettes Guidées (Valeur 147€)",
    "Escute o passo a passo de receitas incríveis na cozinha, sendo guiado durante todo o processo de modo fácil.": "Écoutez pas à pas des recettes incroyables dans la cuisine, en étant guidé facilement tout au long du processus.",
    "Bônus nº 3: Acesso vitalício ao aplicativo (Valor 19€/mês)": "Bonus n° 3 : Accès à vie à l'application (Valeur 19€/mois)",
    "Mantenha o seu guia inteiro no bolso. Fácil de usar, super acessível e totalmente GRÁTIS hoje.": "Gardez tout votre guide dans votre poche. Facile à utiliser, super accessible et totalement GRATUIT aujourd'hui.",
    "Esta é uma oferta única.": "Ceci est une offre unique.",
    "Assim que sair desta página, esses bônus desaparecerão e o Audiobook voltará ao preço normal de 197€.": "Dès que vous quitterez cette page, ces bonus disparaîtront et le Livre Audio reviendra à son prix normal de 197€.",
    "Por ser novo por aqui, você adiciona este pacote completo por <strong>um único pagamento de 29€!</strong>": "Puisque vous êtes nouveau ici, vous ajoutez ce forfait complet pour <strong>un seul paiement de 29€ !</strong>",
    "Garantia de reembolso de 30 dias": "Garantie de remboursement de 30 jours",
    "Garantia de Reembolso de 30 Dias": "Garantie de Remboursement de 30 Jours",
    "Pagamento seguro • Criptografado": "Paiement sécurisé • Crypté",
    "Pago seguro • Pago encriptado": "Paiement sécurisé • Crypté",
    "Atualização verificada": "Mise à jour vérifiée",
    "Melhoria Verificada": "Mise à jour vérifiée",
    "Página de Pedido Segura": "Page de Commande Sécurisée",
    "Página de pedido segura": "Page de Commande Sécurisée",
    "Política de Privacidade": "Politique de Confidentialité",
    "Termos e Condições": "Termes et Conditions",
    
    "'Receitas Ricas em Proteína'": "'Recettes Riches en Protéines'",
    "'Mais de 100 Receitas Proteicas & Low Carb'": "'Plus de 100 Recettes Protéinées & Low Carb'",
    "Audiobook Completo das Receitas Proteicas": "Livre Audio Complet des Recettes Protéinées",
    
    "'Meal Prep para Emagrecer'": "'Meal Prep pour Maigrir'",
    "'Mais de 100 Receitas & Dicas de Refeições'": "'Plus de 100 Recettes & Astuces de Repas'",
    "Audiobook Completo de Meal Prep e Emagrecimento": "Livre Audio Complet de Meal Prep et Perte de Poids",
    
    "'Dieta Completa para Combater a Gordura no Fígado'": "'Régime Complet pour Combattre le Foie Gras'",
    "'Receitas para Gordura no Fígado'": "'Recettes pour le Foie Gras'",
    "'Mais de 100 Receitas para Limpar o Fígado'": "'Plus de 100 Recettes pour Nettoyer le Foie'",
    "Audiobook Completo de Dieta Para Gordura no Fígado": "Livre Audio Complet du Régime Foie Gras",
    "Audiobook Completo de Receitas para o Fígado": "Livre Audio Complet de Recettes pour le Foie",
    
    "'Mais de 100 Receitas & Plano de Refeições'": "'Plus de 100 Recettes & Plan de Repas'",
    "'Dieta Completa para Combater o Diabetes'": "'Régime Complet pour Combattre le Diabète'",
    "Audiobook Completo das Receitas de Diabetes": "Livre Audio Complet des Recettes pour le Diabète",
    
    "⚠️ NÃO FECHE ESTA PÁGINA!": "⚠️ NE FERMEZ PAS CETTE PAGE !",
    "Leve o Audiobook Com Um": "Obtenez le Livre Audio Avec Une",
    "Desconto Exclusivo": "Remise Exclusive",
    "Para tornar esta oferta irresistível, <strong>eu removi o acesso à comunidade privada</strong> (o que reduz meus custos) para entregar a você o <strong>Audiobook Completo das Receitas Proteicas + Áudios de Receitas Passo a Passo</strong>...": "Pour rendre cette offre irrésistible, <strong>j'ai supprimé l'accès à la communauté privée</strong> (ce qui réduit mes coûts) pour vous offrir le <strong>Livre Audio Complet des Recettes Protéinées + Audios de Recettes Pas à Pas</strong>...",
    "Para tornar esta oferta irresistível, <strong>eu removi o acesso à comunidade privada</strong> (o que reduz meus custos) para entregar a você o <strong>Audiobook Completo das Receitas & Meal Prep + Áudios de Receitas Passo a Passo</strong>...": "Pour rendre cette offre irrésistible, <strong>j'ai supprimé l'accès à la communauté privée</strong> (ce qui réduit mes coûts) pour vous offrir le <strong>Livre Audio Complet de Recettes & Meal Prep + Audios de Recettes Pas à Pas</strong>...",
    "Para tornar esta oferta irresistível, <strong>eu removi o acesso à comunidade privada</strong> (o que reduz meus custos) para entregar a você o <strong>Audiobook Completo para Limpar o Fígado + Áudios de Receitas Passo a Passo</strong>...": "Pour rendre cette offre irrésistible, <strong>j'ai supprimé l'accès à la communauté privée</strong> (ce qui réduit mes coûts) pour vous offrir le <strong>Livre Audio Complet pour Nettoyer le Foie + Audios de Recettes Pas à Pas</strong>...",
    "Para tornar esta oferta irresistível, <strong>eu removi o acesso à comunidade privada</strong> (o que reduz meus custos) para entregar a você o <strong>Audiobook Completo de Receitas de Diabetes + Áudios de Receitas Passo a Passo</strong>...": "Pour rendre cette offre irrésistible, <strong>j'ai supprimé l'accès à la communauté privée</strong> (ce qui réduit mes coûts) pour vous offrir le <strong>Livre Audio Complet de Recettes pour le Diabète + Audios de Recettes Pas à Pas</strong>...",
    "Por um pagamento único de apenas 19€!": "Pour un paiement unique de seulement 19€ !",
    "*Clique no botão abaixo para adicionar esse desconto imediato ao seu pedido seguro.": "*Cliquez sur le bouton ci-dessous pour ajouter cette réduction immédiate à votre commande sécurisée.",

    '"O audiobook mudou tudo para mim!"': '"Le livre audio a tout changé pour moi !"',
    '"Minha visão já não é a mesma, então ler na tela era difícil. Este audiobook me permitiu escutar os ensinamentos práticos de como cozinhar proteínas e carboidratos da melhor forma. Preparar as refeições agora ficou super simples!"': '"Ma vue n\'est plus la même, il m\'était donc difficile de lire sur un écran. Ce livre audio m\'a permis d\'écouter des conseils pratiques sur la meilleure façon de cuisiner des protéines et des glucides. Préparer des repas est maintenant devenu très simple !"',
    '"Essas dicas valem cada centavo de 29€."': '"Ces conseils valent chaque centime des 29€."',
    '"Eu estava em dúvida, mas as dicas diárias e os áudios são maravilhosos. Escutar as receitas em vez de ler mudou minha rotina. As receitas com alto teor de proteína me deram muita energia!"': '"J\'hésitais, mais les conseils quotidiens et les audios sont formidables. Écouter les recettes au lieu de les lire a changé ma routine. Les recettes riches en protéines m\'ont donné beaucoup d\'énergie !"',
    
    '"Minha visão já não é a mesma, então ler na tela era difícil. Este audiobook me permitiu escutar todas as ideias de preparação de refeições enquanto vou para o trabalho. Começar a minha reeducação alimentar agora ficou super simples!"': '"Ma vue n\'est plus la même, lire sur un écran était difficile. Ce livre audio m\'a permis d\'écouter toutes les idées de préparation de repas sur le chemin du travail. Commencer ma rééducation alimentaire est devenu super simple !"',
    '"Eu estava em dúvida, mas as dicas diárias de nutrição são maravilhosas. Escutar o passo a passo sobre como preparar minhas marmitas da semana em áudio mudou minha organização de tempo. Recomendo muito!"': '"J\'hésitais, mais les conseils nutritionnels quotidiens sont merveilleux. Écouter le pas à pas sur la façon de préparer mes repas de la semaine en audio a changé mon organisation de temps. Je recommande vivement !"',

    '"Minha visão já não é a mesma, então ler a tela do celular era difícil. Este Audiobook me permitiu fechar os olhos e simplesmente escutar as receitas proteicas. Surpreendentemente prático e fácil de aplicar!"': '"Ma vue n\'est plus la même, lire sur l\'écran du téléphone était difficile. Ce Livre Audio m\'a permis de fermer les yeux et d\'écouter simplement les recettes protéinées. Étonnamment pratique et facile à appliquer !"',
    '"O conhecimento deste áudio vale cada centavo dos 29€."': '"Les connaissances de cet audio valent chaque centime des 29€."',
    '"Fiquei em dúvida sobre adquirir o audiobook de forma isolada, mas o conteúdo é fantástico. Escutar as explicações de nutrição enquanto cozinho me ajudou imensamente a controlar a glicose de forma leve e sem esforço. Recomendo muito!"': '"J\'hésitais à acheter le livre audio seul, mais le contenu est fantastique. Écouter les explications nutritionnelles en cuisinant m\'a énormément aidé à contrôler ma glycémie de manière légère et sans effort. Je recommande vivement !"',
    
    '"Minha visão já não é a mesma, então ler na tela era difícil. Este audiobook me permitiu escutar os métodos práticos para cuidar do fígado. Cuidar da minha saúde agora ficou super simples!"': '"Ma vue n\'est plus la même, il m\'était donc difficile de lire sur un écran. Ce livre audio m\'a permis d\'écouter des méthodes pratiques pour prendre soin de mon foie. Prendre soin de ma santé est maintenant devenu très simple !"',
    '"Eu estava em dúvida, mas as dicas do áudio são maravilhosas. Escutar as receitas recomendadas pela manhã mudou minha forma de me alimentar. Os níveis das minhas enzimas hepáticas até melhoraram!"': '"J\'hésitais, mais les conseils audio sont formidables. Écouter les recettes recommandées le matin a changé ma façon de manger. Les niveaux de mes enzymes hépatiques se sont même améliorés !"',

    '"Minha visão já não é a mesma, então ler na tela era difícil. Este audiobook me permitiu descansar os olhos e apenas escutar os ensinamentos reais de nutrição. Cuidar do diabetes agora ficou super simples e prático!"': '"Ma vue n\'est plus la même, il m\'était donc difficile de lire sur un écran. Ce livre audio m\'a permis de reposer mes yeux et d\'écouter simplement de vrais enseignements nutritionnels. Gérer le diabète est maintenant devenu super simple et pratique !"',
    '"Eu estava em dúvida, mas as dicas diárias no grupo e os áudios são maravilhosos. Escutar as receitas em voz alta ao invés de ficar focado num manual logo mudou minha rotina na cozinha de forma positiva. Recomendo muito."': '"J\'hésitais, mais les conseils quotidiens dans le groupe et les audios sont formidables. Écouter les recettes à voix haute au lieu de me concentrer sur un manuel a rapidement changé ma routine en cuisine de manière positive. Je recommande vivement."'
}

directories = [
    'upproteinafrances', 'upperdadepesofrances', 'upgorduranofigadofrances', 'updiabetesfrances',
    'downdiabeteesfrances', 'downgorduranofigadofrances', 'downperdadepesofrances', 'downproteinafrances'
]

for directory in directories:
    file_path = os.path.join(directory, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Translated {file_path}")
