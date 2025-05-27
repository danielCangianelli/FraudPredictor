import SwiftUI
struct ContentView: View {
    @StateObject private var viewModel = FraudDetectorViewModel()

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Informações da Transação")) {
                    Stepper("Tempo desde última transação: \(Int(viewModel.tempoDesdeUltimaTransacao))s", value: $viewModel.tempoDesdeUltimaTransacao, in: 0...5000)

                    Stepper("Valor da transação: R$ \(Int(viewModel.valorTransacao))", value: $viewModel.valorTransacao, in: 0...10000)

                    Picker("Comerciante de risco", selection: $viewModel.localizacaoComercianteRisco) {
                        Text("Não").tag(0)
                        Text("Sim").tag(1)
                    }

                    Stepper("Frequência do cartão no dia: \(viewModel.frequenciaCartaoDia)", value: $viewModel.frequenciaCartaoDia, in: 0...50)

                    Stepper("Média de gasto semanal: R$ \(Int(viewModel.mediaGastoCartaoSemana))", value: $viewModel.mediaGastoCartaoSemana, in: 0...10000)
                }

                Button("Verificar Fraude") {
                    viewModel.preverFraude()
                }

                if !viewModel.resultado.isEmpty {
                    Section(header: Text("Resultado")) {
                        Text(viewModel.resultado).font(.headline)
                    }
                }
            }
            .navigationTitle("Detector de Fraude")
        }
    }
}
#Preview {
    ContentView()
}
