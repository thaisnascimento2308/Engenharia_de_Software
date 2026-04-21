<?php include('layouts/header.php'); ?>

<div class="container mt-5">
    <h1>Descubra seu Signo</h1>

    <form method="POST" action="show_zodiac_sign.php">
        <div class="mb-3">
            <label class="form-label">Data de Nascimento</label>

            <input 
                type="date" 
                class="form-control" 
                name="data_nascimento" 
                required
            >
        </div>

        <button type="submit" class="btn btn-primary">
            Descobrir
        </button>
    </form>
</div>