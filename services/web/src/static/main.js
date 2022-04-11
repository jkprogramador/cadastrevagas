$(function () {
    const $data_hora_entrevista_el = $('#id_data_hora_entrevista');
    const $situacao_el = $('#id_situacao');

    if ('C' === $situacao_el.val()) {
        $data_hora_entrevista_el.prop('disabled', true);
    }

    $data_hora_entrevista_el.datetimepicker({
        language: 'pt-BR',
        rtl: false,
        pickerPosition: 'bottom-right',
        minuteStep: 5,
        initialDate: new Date(),
        format: 'dd/mm/yyyy hh:ii',
        weekStart: 1,
        todayHighlight: true,
        autoclose: true,
    });

    $situacao_el.change(function (el) {
        situacao = el.target.value;

        if ('C' === situacao) {
            $data_hora_entrevista_el.prop('disabled', true).val('');
        } else {
            $data_hora_entrevista_el.prop('disabled', false);
        }
    });

    $('#id_empresa_telefone_celular').mask('(00) 00000-0000', { placeholder: '(DDD) _____-____' });
    $('#id_empresa_telefone_comercial').mask('(00) 0000-0000', { placeholder: '(DDD) ____-____' });
});