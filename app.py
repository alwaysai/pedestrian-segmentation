import edgeiq
import numpy as np


def main():
    semantic_segmentation = edgeiq.SemanticSegmentation(
            "alwaysai/enet")
    semantic_segmentation.load(engine=edgeiq.Engine.DNN)

    print("Engine: {}".format(semantic_segmentation.engine))
    print("Accelerator: {}\n".format(semantic_segmentation.accelerator))
    print("Model:\n{}\n".format(semantic_segmentation.model_id))
    print("Labels:\n{}\n".format(semantic_segmentation.labels))

    labels_to_mask = ['Person', 'Rider', 'Bicycle', 'Motorcycle']
    print("Labels to mask:\n{}\n".format(labels_to_mask))

    enable_streamer = False

    with edgeiq.FileVideoStream('Use Case - Clip 3.mp4') as video_stream, \
            edgeiq.VideoWriter(output_path="processed_video.avi") as video_writer:

        if enable_streamer:
            streamer = edgeiq.Streamer().setup()

        last_non_detection = None
        while video_stream.more():
            frame = video_stream.read()

            if last_non_detection is None:
                last_non_detection = np.zeros(frame.shape)

            results = semantic_segmentation.segment_image(frame)

            if enable_streamer:
                # Generate text to display on streamer
                text = ["Model: {}".format(semantic_segmentation.model_id)]
                text.append("Inference time: {:1.3f} s".format(results.duration))
                text.append("Legend:")
                text.append(semantic_segmentation.build_legend())

            label_map = np.array(semantic_segmentation.labels)[results.class_map]
            # Setting to zero defaults to "Unlabeled"
            filtered_class_map = np.zeros(results.class_map.shape).astype(int)
            for label in labels_to_mask:
                filtered_class_map += results.class_map * (label_map == label).astype(int)

            non_detection_map = (filtered_class_map == 0)
            detection_map = (filtered_class_map != 0)
            last_non_detection[non_detection_map] = frame[non_detection_map].copy()
            out_frame = frame.copy()
            out_frame[detection_map] = last_non_detection[detection_map].copy()

            if enable_streamer:
                combined = np.concatenate((frame, out_frame), axis=0)

                streamer.send_data(combined, text)
                if streamer.check_exit():
                    break

            video_writer.write_frame(out_frame)

        if enable_streamer:
            streamer.close()

        print("Program Ending")


if __name__ == "__main__":
    main()
