import SwiftUI
import CoreML

// MARK: - ViewModel
class FraudDetectorViewModel: ObservableObject {
    @Published var tempoDesdeUltimaTransacao: Double = 10
    @Published var valorTransacao: Double = 800
    @Published var localizacaoComercianteRisco: Int = 1
    @Published var frequenciaCartaoDia: Int = 12
    @Published var mediaGastoCartaoSemana: Double = 450

    @Published var resultado: String = ""

    func preverFraude() {
        do {
            let model = try ModeloFraude(configuration: MLModelConfiguration())

            let input = ModeloFraudeInput(
                tempo_desde_ultima_transacao: tempoDesdeUltimaTransacao,
                valor_transacao: valorTransacao,
                localizacao_comerciante_risco: Int64(localizacaoComercianteRisco),
                frequencia_cartao_dia: Int64(frequenciaCartaoDia),
                media_gasto_cartao_semana: mediaGastoCartaoSemana
            )

            let prediction = try model.prediction(input: input)

            if prediction.fraude == 1 {
                resultado = "⚠️ Fraude detectada"
            } else {
                resultado = "✅ Transação legítima"
            }
        } catch {
            resultado = "Erro ao fazer a previsão: \(error.localizedDescription)"
        }
    }
}
