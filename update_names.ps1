$replacements = @{
    "upproteinafrances" = "Pack Ultime : Recettes Protéinées Low Carb"
    "upproteinaitaliano" = "Pacchetto Definitivo: Ricette Proteiche e Low Carb"
    "upproteinaalemao" = "Das ultimative Paket: Proteinreiche Low-Carb-Rezepte"
    "upperdadepesofrances" = "Pack Ultime : Meal Prep pour Maigrir"
    "upperdadepesoitaliano" = "Pacchetto Finale: Meal Prep per Dimagrire"
    "upperdadepesoalemao" = "Das ultimative Paket: Meal Prep zum Abnehmen"
    "upgorduranofigadofrances" = "Le Livre de Recettes Complet pour le Foie Gras pour Débutants"
    "upgorduranofigadoitaliano" = "Il Ricettario Completo per la Dieta del Fegato Grasso per Principianti"
    "upgorduranofigadoalemao" = "Das Komplette Fettleber-Diät-Kochbuch für Anfänger"
    "updiabetesfrances" = "Le régime diabétique le plus facile après 60 ans"
    "updiabetesitaliano" = "La Dieta più Semplice per Diabetici Dopo i 60 Anni"
    "updiabetesalemao" = "Die Einfachste Diabetiker-Diät Nach 60"
    "updiabetesportugues" = "A Dieta para Diabéticos Mais Fácil Após os 60"
    "updiabetesarabe" = "أسهل نظام غذائي لمرضى السكري بعد الستين"
    "updiabetesespanhol" = "La Dieta para Diabéticos más fácil después de los 60"
    "updiabetespolones" = "Najprostsza Dieta Dla Diabetyków Po 60-tce"
    "updiabetesholandes" = "Het Eenvoudigste Diabetisch Dieet Na 60"
}

foreach ($entry in $replacements.GetEnumerator()) {
    $dir = $entry.Name
    $newName = $entry.Value
    $path = ".\$dir\index.html"
    
    if (Test-Path $path) {
        $content = Get-Content $path -Raw -Encoding UTF8
        
        # Replace in H1
        $content = [regex]::Replace($content, "(<span style=`"font-weight: 400;`">[^<]+</span>\s*)'([^']+)'", "`$1'$newName'")
        
        # Replace in Paragraph
        $content = [regex]::Replace($content, "(<strong>[^<]*?)'([^']+)'(</strong>)", "`$1'$newName'`$3")
        
        [System.IO.File]::WriteAllText("C:\Users\Usuario\Downloads\upsellbook-main\upsellbook-main\$dir\index.html", $content, (New-Object System.Text.UTF8Encoding($false)))
        Write-Host "Updated $dir with '$newName'"
    } else {
        Write-Host "Warning: $path not found"
    }
}
Write-Host "All replacements completed."
