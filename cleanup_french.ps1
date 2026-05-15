$dirs = Get-ChildItem -Directory | Where-Object { $_.Name -match "^(up|down).*(italiano|alemao|arabe|espanhol|holandes|polones)$" }

foreach ($dir in $dirs) {
    $lang = $dir.Name -replace "^(up|down)(diabetes|proteina|gorduranofigado|perdadepeso)", ""
    $path = "$($dir.FullName)\index.html"
    if (Test-Path $path) {
        $content = Get-Content $path -Raw -Encoding UTF8
        
        if ($lang -eq "italiano") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "Proprio ora, hai l'opportunità esclusiva di migliorare il tuo ordine e ottenere la versione completa in")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"La mia vista non è più la stessa, quindi leggere sullo schermo era difficile. Questo audiolibro mi ha permesso")
        }
        if ($lang -eq "alemao") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "Genau jetzt haben Sie die exklusive Gelegenheit, Ihre Bestellung aufzuwerten und die Vollversion als")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"Meine Sehkraft ist nicht mehr dieselbe, also war das Lesen auf dem Bildschirm schwierig. Dieses Hörbuch hat es mir ermöglicht,")
        }
        if ($lang -eq "espanhol") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version completa en", "En este momento, tienes la oportunidad exclusiva de mejorar tu pedido y obtener la versión completa en")
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "En este momento, tienes la oportunidad exclusiva de mejorar tu pedido y obtener la versión completa en")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"Mi vista ya no es la misma, por lo que leer en la pantalla era difícil. Este audiolibro me permitió")
        }
        if ($lang -eq "holandes") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "Op dit moment heeft u de exclusieve kans om uw bestelling te upgraden en de volledige versie te krijgen als")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"Mijn zicht is niet meer hetzelfde, dus lezen op het scherm was moeilijk. Dit audioboek stelde me in staat om")
        }
        if ($lang -eq "polones") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "Właśnie teraz masz ekskluzywną okazję, aby ulepszyć swoje zamówienie i uzyskać pełną wersję jako")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"Mój wzrok nie jest już taki sam, więc czytanie na ekranie było trudne. Ten audiobook pozwolił mi")
        }
        if ($lang -eq "arabe") {
            $content = $content.Replace("En ce moment, vous avez l'opportunité exclusive d'améliorer votre commande et d'obtenir la version complète en", "الآن، لديك فرصة حصرية لترقية طلبك والحصول على النسخة الكاملة كـ")
            $content = $content.Replace("`"Ma vue n'est plus la même, il m'était donc difficile de lire sur un écran. Ce livre audio m'a permis", "`"لم تعد رؤيتي كما كانت، لذا كان القراءة على الشاشة أمراً صعباً. أتاح لي هذا الكتاب الصوتي")
        }

        [System.IO.File]::WriteAllText($path, $content, (New-Object System.Text.UTF8Encoding($false)))
    }
}
Write-Host "Cleanup done!"
