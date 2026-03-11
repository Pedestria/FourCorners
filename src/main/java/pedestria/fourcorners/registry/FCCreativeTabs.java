package pedestria.fourcorners.registry;

import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import pedestria.fourcorners.FourCorners;

public final class FCCreativeTabs {
    public static final DeferredRegister<CreativeModeTab> CREATIVE_MODE_TABS =
            DeferredRegister.create(Registries.CREATIVE_MODE_TAB, FourCorners.MODID);

    public static final RegistryObject<CreativeModeTab> FOUR_CORNERS_TAB =
            CREATIVE_MODE_TABS.register(
                    "four_corners",
                    () ->
                            CreativeModeTab.builder()
                                    .title(Component.translatable("itemGroup.fourcorners"))
                                    .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
                                    .icon(() -> FCItems.WISDOM_INGOT.get().getDefaultInstance())
                                    .displayItems(
                                            (parameters, output) -> {
                                                output.accept(FCItems.START_TOME.get());
                                                output.accept(FCItems.WISDOM_SHARD.get());
                                                output.accept(FCItems.AVALON_GEM.get());
                                                output.accept(FCItems.WISDOM_INGOT.get());
                                                output.accept(FCItems.AVALON_INGOT.get());
                                                output.accept(FCBlocks.AVALITE_ORE_BLOCK.get());
                                                output.accept(FCBlocks.WISDOM_ORE_BLOCK.get());
                                                output.accept(FCBlocks.DIMENSION_ACCESSOR_BLOCK.get());
                                                output.accept(FCBlocks.CORE_FABRICATOR_SIMPLE_BLOCK.get());
                                            })
                                    .build());

    private FCCreativeTabs() {}
}
