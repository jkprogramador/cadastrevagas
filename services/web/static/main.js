$(function() {
    const $data_hora_entrevista_el = $('#id_data_hora_entrevista');
    const $situacao_el = $('#id_situacao');

    if ('W' === $situacao_el.val()) {
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

    $situacao_el.change(function(el) {
        situacao = el.target.value;

        if ('W' === situacao) {
            $data_hora_entrevista_el.prop('disabled', true).val('');
        } else {
            $data_hora_entrevista_el.prop('disabled', false);
        }
    });
});