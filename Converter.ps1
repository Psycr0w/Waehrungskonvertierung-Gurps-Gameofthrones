param(
    [int]$Gurpsdollar,
    [Switch]$Md
)
$Drachendiv = 23520
$Mondediv = 784
$hirschendiv = 112
$Sternediv = 16
$Groschendiv = 8
$Halbgroschendiv = 4
$penniesdiv = 2
$Halbpennies = $Gurpsdollar

$monde = 0
$monddolar = 0

$drachen = [int][Math]::Floor($gurpsdollar / $Drachendiv)
$drachendollar = $drachen * $drachendiv
if ($Md -eq $true)
{
    $monde = [int][Math]::Floor(($Gurpsdollar - $drachendollar) / $Mondediv)
    $monddolar = $monde * $Mondediv
}
$hirschen = [int][Math]::Floor((($Gurpsdollar -$drachendollar - $monddolar)) / $hirschendiv)
$hirschdollar = $hirschen * $hirschendiv
$sterne = [int][Math]::Floor((($Gurpsdollar - $drachendollar - $monddolar - $hirschdollar)) / $Sternediv)
$sterndollar = $sterne * $Sternediv
$groschen = [int][Math]::Floor((($Gurpsdollar - $drachendollar  - $monddolar - $hirschdollar - $sterndollar)) / $Groschendiv)
$groschendollar = $groschen * $Groschendiv
$halbgroschen = [int][Math]::Floor((($Gurpsdollar - $drachendollar  - $monddolar - $hirschdollar - $sterndollar - $groschendollar)) / $Halbgroschendiv)
$halbgroschendollar = $halbgroschen * $Halbgroschendiv
$pennies = [int][Math]::Floor((($Gurpsdollar - $drachendollar  - $monddolar - $hirschdollar - $sterndollar - $groschendollar - $halbgroschendollar)) / $penniesdiv)
$penniesdollar = $pennies * $penniesdiv
$halbpennies = $Gurpsdollar - $drachendollar  - $monddolar - $hirschdollar - $sterndollar - $groschendollar - $halbgroschendollar - $penniesdollar


$currency =
"Drachen",
"Monde",
"Hirschen",
"Sterne",
"Groschen",
"Halbgroschen",
"Pennies",
"Halbpennies"

$value =
$drachen,
$monde,
$hirschen,
$sterne,
$groschen,
$halbgrosche,
$pennies,
$Halbpennies

$array = @()

for ($i=0;$i -lt $currency.Length;$i++)
{
    if ($value[$i]-gt 0)
    {
        $val = $value[$i]
        $cur = $currency[$i]
        $array += "$val $cur"
    }
         
}

$string = $array -join " , "

Write-Output $string