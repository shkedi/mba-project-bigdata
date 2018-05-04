from sklearn.preprocessing import MinMaxScaler


def normelized(input):
    scaler = MinMaxScaler(feature_range=(0, 1))
    gifts = []
    values = []
    rest = []
    avg = []
    feedback = []

    for raw in input:
        gifts.append(raw[0:3])
        values.append(raw[3:16])
        rest.append(raw[16:20])
        avg.append(raw[20:22])
        if len(raw) == 23:
            feedback.append([raw[22]])
        else:
            feedback.append([])

    normelize_values = scaler.fit_transform(values)
    normelize_avg = scaler.fit_transform(avg)
    normelized_x = []
    for i in range(len(input)):
        normelized_x.append(gifts[i] + list(normelize_values[i]) + rest[i] + list(normelize_avg[i]) + feedback[i])

    return normelized_x
