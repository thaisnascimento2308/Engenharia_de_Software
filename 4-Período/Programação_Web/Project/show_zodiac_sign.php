<?php include('layouts/header.php'); ?>

<div class="container mt-5">
<?php

ini_set('display_errors', 1);
error_reporting(E_ALL);

$data_nascimento = $_POST['data_nascimento'] ?? null;

if (!$data_nascimento) {
    echo "<div class='alert alert-danger'>Data não informada.</div>";
    exit;
}

$data_formatada = (new DateTime($data_nascimento))->format('d/m/Y');

// Data usuário
$date_obj = new DateTime($data_nascimento);
$mes_dia_usuario = (int)$date_obj->format('md');

// XML
$signos = simplexml_load_file(__DIR__ . "/signos.xml");

if ($signos === false) {
    die("<div class='alert alert-danger'>Erro ao carregar XML.</div>");
}

$signo_encontrado = null;

foreach ($signos->signo as $signo) {

    $inicio_xml = explode('/', (string)$signo->dataInicio);
    $fim_xml    = explode('/', (string)$signo->dataFim);

    $inicio = (int)sprintf("%02d%02d", (int)$inicio_xml[1], (int)$inicio_xml[0]);
    $fim    = (int)sprintf("%02d%02d", (int)$fim_xml[1], (int)$fim_xml[0]);

    if ($inicio <= $fim) {
        if ($mes_dia_usuario >= $inicio && $mes_dia_usuario <= $fim) {
            $signo_encontrado = $signo;
            break;
        }
    } else {
        if ($mes_dia_usuario >= $inicio || $mes_dia_usuario <= $fim) {
            $signo_encontrado = $signo;
            break;
        }
    }
}
?>

<?php if ($signo_encontrado): ?>
    <div class="card p-5 text-center shadow">

        <p class="text-muted">
            Data informada: <strong><?= $data_formatada ?></strong>
        </p>

        <h2 class="text-primary">
            Seu signo é: <strong><?= $signo_encontrado->signoNome ?></strong>
        </h2>

        <hr>

        <p class="lead mt-3">
            <?= $signo_encontrado->descricao ?>
        </p>

    </div>
<?php else: ?>
    <div class="alert alert-warning text-center">
        Signo não encontrado para a data: <strong><?= $data_formatada ?></strong>
    </div>
<?php endif; ?>

<div class="text-center mt-4">
    <a href="index.php" class="btn btn-secondary">Voltar</a>
</div>

</div>

</body>
</html>